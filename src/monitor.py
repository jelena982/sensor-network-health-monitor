import pandas as pd
from datetime import datetime

LATENCY_THRESHOLD = 1000 
DATA_QUALITY_THRESHOLD = 0.8  
DATA_FILE = 'data/sensor_status.csv'

try:
  df = pd.read_csv(DATA_FILE)
except FileNotFoundError:
   print(f"Error: The file '{DATA_FILE}' was not found.")
   exit()

healthy_count = 0
warning_count = 0
critical_count = 0
no_data_count = 0
unknown_status_count = 0

def check_sensor_status(row):

    if row['status'] not in ['ONLINE', 'OFFLINE', 'ERROR']:
        return "Unknown Status"

    if row['status'] == "OFFLINE":
          return "CRITICAL"
    elif row['status'] == 'ERROR':
          return "CRITICAL"
    if pd.isna(row['latency_ms']) and pd.isna(row['data_quality']):
        return "No Data available for Latency and Data Quality"
    elif pd.isna(row['latency_ms']):
        return "No Data available for Latency"
    elif pd.isna(row['data_quality']):
       return "No Data available for Data Quality"
    elif row['status'] == 'ONLINE' and  (row['latency_ms'] >= LATENCY_THRESHOLD or row['data_quality'] <= DATA_QUALITY_THRESHOLD):
          return "WARNING"
    else:
      return "HEALTHY"

def get_warning_reason(row):
     if row['status']=="ONLINE":
        if row['latency_ms'] >= LATENCY_THRESHOLD and row['data_quality'] <= DATA_QUALITY_THRESHOLD:
            return 'High Latency and Low Data Quality detected'
        elif row['latency_ms'] >= LATENCY_THRESHOLD:
            return 'High Latency detected'
        elif row['data_quality'] <= DATA_QUALITY_THRESHOLD:
            return 'Low Data Quality Detected'

report_lines=[]
for _, row in df.iterrows():
    result = check_sensor_status(row)
    
    print(row['sensor_id'], row['status'])
    print(result)
    
    if result == "HEALTHY":
        healthy_count += 1
        line = f"{row['sensor_id']} - {result} - Sensor {row['status']}"
    elif result == "WARNING":
        reason = get_warning_reason(row)
        print(reason)
        warning_count += 1
        line = f"{row['sensor_id']} - {result} - {reason}"
    elif result == "CRITICAL":
        critical_count += 1
        line = f"{row['sensor_id']} - {result} - Sensor {row['status']}"
    elif result.startswith("No Data available"):
        no_data_count += 1
        line = f"{row['sensor_id']} - {result}"
    elif result == "Unknown Status":
        unknown_status_count += 1
        line = f"{row['sensor_id']} - {result}"
    
    report_lines.append(line)
print(f"Healthy: {healthy_count}, Warning: {warning_count}, Critical: {critical_count}, No Data: {no_data_count}, Unknown Status: {unknown_status_count}")

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('reports/sensor_report.txt', 'w') as file:
    file.write(f"Sensor Network Health Report\nGenerated on: {current_time}\n\n")

    for line in report_lines:
        file.write(line + "\n")

    file.write(
        f"\nSummary:\n"
        f"Healthy: {healthy_count}\n"
        f"Warning: {warning_count}\n"
        f"Critical: {critical_count}\n"
        f"No Data: {no_data_count}\n"
        f"Unknown Status: {unknown_status_count}\n"
    )
