# Sensor Network Health Monitor

## Overview

Sensor Network Health Monitor is a small Python project that simulates basic monitoring of a distributed sensor network using synthetic sensor data.

The program reads sensor information from a CSV file, evaluates the health of each sensor based on predefined thresholds, detects missing data, identifies possible issues, and generates a timestamped health report.

The project was created to practice Python, data processing, monitoring logic, troubleshooting, and basic automation concepts.

## Features

- Reads sensor status data from a CSV file
- Classifies sensors as HEALTHY, WARNING, or CRITICAL
- Detects high latency and low data quality
- Detects missing latency and data quality values
- Identifies OFFLINE and ERROR sensor states
- Provides a reason for detected warnings
- Counts sensors by health category
- Generates a timestamped text report
- Handles missing input files using Python exception handling

## Monitoring Rules

The project uses the following simulated monitoring rules:

- **CRITICAL**: Sensor status is OFFLINE or ERROR
- **WARNING**: Sensor is ONLINE and latency is at least 1000 ms or data quality is 0.8 or lower
- **HEALTHY**: Sensor is ONLINE and no warning conditions are detected
- **No Data**: Latency, data quality, or both values are missing

The thresholds used in this project are defined for demonstration purposes and do not represent thresholds from a real sensor network.

## Project Structure

```text
sensor-network-health-monitor/
│
├── data/
│   └── sensor_status.csv
│
├── src/
│   └── monitor.py
│
├── reports/
│   └── sensor_report.txt
│
├── .gitignore
└── README.md
```

## Technologies

- Python
- pandas
- CSV data processing
- Python datetime
- File handling
- Exception handling

## Example Output

```text
Sensor Network Health Report
Generated on: 2026-09-22 11:55:15

sensor_1 - HEALTHY - Sensor ONLINE
sensor_2 - WARNING - High Latency detected
sensor_3 - CRITICAL - Sensor OFFLINE
sensor_4 - WARNING - Low Data Quality Detected
sensor_5 - CRITICAL - Sensor ERROR
sensor_6 - WARNING - High Latency and Low Data Quality detected
sensor_7 - No Data available for Latency
sensor_8 - No Data available for Latency and Data Quality
sensor_9 - No Data available for Data Quality

Summary:
Healthy: 1
Warning: 3
Critical: 2
No Data: 3
```

## How to Run

Install pandas if it is not already installed:

```bash
pip install pandas
```

Run the monitoring script:

```bash
python src/monitor.py
```

The program analyzes the sensor data and generates a health report in the `reports` directory.

## Purpose

This project demonstrates foundational skills relevant to technical operations and monitoring environments, including data validation, health-status classification, basic anomaly detection, troubleshooting logic, and automated report generation.
