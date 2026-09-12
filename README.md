# 🚦 Smart Traffic Management System

An AI-powered Smart Traffic Management System that uses **YOLOv8** and **OpenCV** for real-time vehicle detection, vehicle counting, traffic density analysis, adaptive signal management, and live dashboard monitoring.

The system processes traffic video, detects vehicles, calculates traffic conditions, and presents the results through a web-based dashboard.

---

## ✨ Features

- 🚗 Real-time vehicle detection using YOLOv8
- 🔢 Automatic vehicle counting
- 📊 Traffic density analysis
- 🚦 Adaptive traffic signal management
- 📺 Live traffic video streaming
- 📈 Real-time analytics and graphs
- 🚨 Emergency monitoring
- 📋 Traffic report generation
- 📤 Report export functionality
- ⚙️ System settings
- 🌐 Web-based monitoring dashboard

---

## 🛠️ Technologies Used

### Backend
- Python
- FastAPI
- Uvicorn

### AI & Computer Vision
- YOLOv8
- Ultralytics
- OpenCV

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### Development Tools
- Visual Studio Code
- Git
- GitHub

---

## 🏗️ System Architecture

```text
Traffic Video
     ↓
YOLOv8 Vehicle Detection
     ↓
Vehicle Counting
     ↓
Traffic Density Analysis
     ↓
Signal Decision / Traffic Management
     ↓
FastAPI Backend
     ↓
Web Dashboard
     ↓
Analytics & Reports
```

---

## 📂 Project Structure

```text
SmartTrafficSystem/
│
├── backend/
│   ├── datasets/
│   │   └── traffic_sample.mp4
│   │
│   ├── routes/
│   │   └── traffic_api.py
│   │
│   ├── services/
│   │   └── video_stream.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   │
│   │   └── js/
│   │       └── app.js
│   │
│   ├── templates/
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── analytics.html
│   │   ├── emergency.html
│   │   ├── reports.html
│   │   ├── settings.html
│   │   └── signal.html
│   │
│   └── main.py
│
├── test_video.py
├── yolov8n.pt
├── README.md
└── .gitignore
```

---

## ⚙️ Requirements

- Python 3.11+
- VS Code
- Modern web browser
- Minimum 8 GB RAM recommended

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/abdulroufe28/SmartTrafficSystem.git
```

### 2. Open the project

```bash
cd SmartTrafficSystem
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### 5. Install required packages

```bash
pip install fastapi uvicorn opencv-python ultralytics jinja2
```

---

## ▶️ Run the Application

Start the FastAPI server using:

```bash
uvicorn backend.main:app --reload
```

After starting the server, open:

```text
http://127.0.0.1:8000
```

---

## 📺 Live Traffic Monitoring

The system processes the configured traffic video and uses YOLOv8 to identify vehicles in the video frames.

Detected vehicles are displayed with bounding boxes and class labels.

Example vehicle classes include:

- Car
- Bus
- Truck
- Motorcycle

The detected vehicle count is used for traffic monitoring and density analysis.

---

## 📊 Dashboard

The dashboard provides a centralized view of the traffic system.

It displays:

- Total vehicle count
- Traffic density
- Emergency monitoring
- Active junction information
- Live traffic video
- Traffic density graphs
- Vehicle distribution
- Traffic alerts

---

## 📈 Analytics

The Analytics module provides graphical representation of traffic information.

It helps monitor:

- Vehicle count
- Traffic density
- Vehicle distribution
- Traffic trends

---

## 🚦 Traffic Signal Management

The system uses vehicle traffic information to support adaptive traffic signal management.

Traffic conditions are categorized based on the detected vehicle count, allowing the system to determine suitable signal timing.

---

## 🚨 Emergency Monitoring

The Emergency module provides a dedicated interface for monitoring emergency-related traffic events and displaying alerts within the traffic management system.

---

## 📋 Reports

The Reports module provides traffic-related information in a structured format.

The system also supports report export functionality for further analysis and documentation.

---

## 🎯 Project Objective

The main objective of this project is to develop an intelligent traffic management platform that combines **AI-based vehicle detection, traffic analysis, adaptive signal management, and web-based monitoring** to support more efficient traffic management.

---

## 🔮 Future Enhancements

- Real-time CCTV camera integration
- Dedicated ambulance detection model
- Multi-junction real-time monitoring
- Database integration for historical traffic data
- Advanced AI-based signal optimization
- Cloud deployment
- IoT-based traffic signal integration
- Real-time GPS-based emergency vehicle tracking

---

## 📜 License

This project was developed as an academic project for learning and demonstration purposes.
