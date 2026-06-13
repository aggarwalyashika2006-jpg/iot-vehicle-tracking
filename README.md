# 🚗 IoT Vehicle Tracking & Theft Prevention System

## 📌 Overview

The **IoT Vehicle Tracking & Theft Prevention System** is an industry-oriented IoT project designed to monitor vehicle location, detect unauthorized movement, and generate alerts in real time. The system combines GPS-based vehicle tracking, geofencing, cloud connectivity, data logging, and dashboard visualization to provide an effective vehicle security solution.

This project demonstrates practical applications of IoT, Embedded Systems, Cloud Computing, Data Analytics, and Real-Time Monitoring.

---

## 🎯 Problem Statement

Vehicle theft and lack of real-time monitoring are major concerns for vehicle owners, logistics companies, fleet operators, and transportation services.

The objective of this project is to:

* Track vehicle location continuously.
* Monitor vehicle movement.
* Detect unauthorized movement.
* Generate theft alerts.
* Maintain location history.
* Visualize data through an interactive dashboard.
* Upload tracking data to a cloud platform.

---

## 🚀 Features

### Vehicle Tracking

* Real-time vehicle location monitoring.
* GPS coordinate simulation and tracking.

### Theft Prevention

* Geofence-based theft detection.
* Unauthorized movement alerts.

### Dashboard Visualization

* Live vehicle status.
* Interactive location map.
* Distance analytics.
* Historical movement records.

### Cloud Integration

* ThingSpeak cloud connectivity.
* Remote monitoring capabilities.

### Data Logging

* CSV-based location history storage.
* Alert history tracking.

### Report Generation

* Automated PDF report creation.
* Tracking summary generation.

### Simulation Support

* Hardware-independent implementation.
* Wokwi ESP32 simulation support.

---

## 🏗️ System Architecture

```text
GPS Module / GPS Simulation
            │
            ▼
         ESP32
            │
            ▼
     Tracking Engine
            │
            ├────────────► Geofence Detection
            │
            ├────────────► Theft Detection
            │
            └────────────► Alert System
            │
            ▼
       Data Logging
            │
            ▼
      Cloud Platform
      (ThingSpeak)
            │
            ▼
    Streamlit Dashboard
            │
            ▼
       User Monitoring
```

---

## 🛠️ Technology Stack

### Hardware

* ESP32 DevKit V1
* NEO-6M GPS Module (Optional)
* LED Indicator
* Piezo Buzzer

### Software

* Python
* Streamlit
* Pandas
* FPDF2
* Requests
* Wokwi Simulator

### Cloud

* ThingSpeak

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
IoT-Vehicle-Tracking-Theft-Prevention-System/

│
├── arduino_code/
│
├── python_simulation/
│   ├── gps_simulator.py
│   ├── geofence.py
│   ├── theft_detector.py
│   ├── distance_calculator.py
│   ├── logger.py
│   ├── report_generator.py
│   └── thingspeak_uploader.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── location_log.csv
│
├── outputs/
│
├── reports/
│   └── Vehicle_Report.pdf
│
├── images/
│
├── docs/
│
├── requirements.txt
│
├── main.py
│
└── README.md
```

---

## ⚙️ Installation

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Start Vehicle Simulation

```bash
python main.py
```

This generates:

* Vehicle coordinates
* Geofence events
* Theft alerts
* CSV logs

---

### Generate PDF Report

```bash
python python_simulation/report_generator.py
```

Output:

```text
reports/Vehicle_Report.pdf
```

---

### Run Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard Features:

* Vehicle status monitoring
* Interactive map
* Alert display
* Movement analytics
* Historical records

---

## ☁️ ThingSpeak Cloud Setup

1. Create a ThingSpeak account.
2. Create a new channel.
3. Configure fields:

| Field   | Description |
| ------- | ----------- |
| Field 1 | Latitude    |
| Field 2 | Longitude   |
| Field 3 | Distance    |
| Field 4 | Status Code |

4. Copy Write API Key.
5. Update:

```python
WRITE_API_KEY = "DDFC2ML9CF0KX5Z0"
```

6. Run:

```bash
python main.py
```

Data will automatically be uploaded to ThingSpeak.

---

## 📊 Dashboard Features

### Live Metrics

* Latitude
* Longitude
* Distance
* Vehicle Status

### Analytics

* Distance trend
* Latitude trend
* Longitude trend

### Alerts

* Safe state monitoring
* Theft alert visualization

### Location Monitoring

* Live map view
* Historical movement tracking

---

## 🔔 Theft Detection Logic

The project uses geofencing.

### Safe Zone

```text
Vehicle inside geofence
```

Status:

```text
MOVING SAFELY
```

### Theft Scenario

```text
Vehicle exits geofence
```

Status:

```text
THEFT SUSPECTED
```

Actions:

* Alert generated
* Dashboard updated
* Cloud data updated
* Event logged

---

## 📄 Report Generation

Generated report contains:

* Total records
* Safe movement count
* Theft alert count
* Parked records
* Recent tracking history

Output:

```text
Vehicle_Report.pdf
```

---

## 🧪 Wokwi Simulation

The project includes ESP32 simulation using Wokwi.

### Components

* ESP32 DevKit V1
* LED
* Piezo Buzzer

### Simulated Features

* Vehicle tracking
* Geofence detection
* Theft alert indication

---

## 💼 Industry Applications

### Logistics Companies

* Fleet monitoring
* Route optimization

### Delivery Services

* Vehicle tracking
* Driver monitoring

### School Transportation

* School bus tracking
* Safety monitoring

### Personal Vehicles

* Theft prevention
* Recovery support

### Trucking Industry

* Fleet management
* Cargo security

---

## 🔮 Future Enhancements

* Real GPS module integration
* GSM/SMS alert system
* Mobile application
* MQTT communication
* Node-RED dashboard
* Firebase integration
* AI-based theft prediction
* Route optimization
* Driver behavior analytics

---

## 🎓 Learning Outcomes

This project demonstrates:

* Internet of Things (IoT)
* Embedded Systems
* Cloud Computing
* Geofencing
* Data Analytics
* Dashboard Development
* Python Programming
* ESP32 Programming
* GitHub Project Management

---

## Link-

## 👩‍💻 Author

**Yashika Aggarwal**

Electronics & Communication Engineering Student

IoT | Embedded Systems | Data Analytics | Software Development

---

## ⭐ If You Like This Project

Give this repository a star and share your feedback.

---

## 📜 License

This project is developed for educational and academic purposes.
