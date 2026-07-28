# Blink Reminder System

## Project Title

**Blink Reminder System Using Computer Vision**

## Project Overview

The Blink Reminder System is a computer vision-based application designed to help users maintain healthy eye habits while using a computer for long periods. The system uses a webcam to detect the user's eyes and monitor prolonged eye fixation. If the user's eyes remain focused for longer than the defined threshold, the system displays a warning message and plays an alarm sound as a reminder to take a break or blink.

This project aims to reduce eye strain and encourage better digital eye-care habits through real-time computer vision and audio alerts.

## Features

- Real-time webcam-based eye detection
- Eye detection using OpenCV Haar Cascade Classifier
- Monitors prolonged eye fixation
- Displays gaze duration on the screen
- Shows an alert when eyes remain fixed for too long
- Plays an alarm sound as a reminder
- Uses an external Haar Cascade XML file for reliable eye detection
- Simple and lightweight Python-based implementation

## Technologies Used

- **Python 3.10**
- **OpenCV**
- **Pygame**
- **NumPy**
- **Computer Vision**
- **Haar Cascade Classifier**
- **Webcam**

## Project Structure

```text
blink-reminder-system/
│
├── alerts/
│   ├── __init__.py
│   └── alert_system.py
│
├── detection/
│   ├── __init__.py
│   └── eye_detection.py
│
├── sound/
│   └── alarm.wav
│
├── utils/
│
├── screenshots/
│
├── haarcascade_eye.xml
├── main.py
├── requirements.txt
├── test_sound.py
├── .gitignore
└── README.md

Future Enhancements
Improve eye detection accuracy using MediaPipe Face Mesh
Add automatic blink detection
Add eye exercise recommendations
Add configurable fixation time thresholds
Add daily eye-care statistics and reports
Add a graphical user interface (GUI)
Add desktop notifications
Add user activity and health logs
Add machine learning-based eye fatigue detection
Support multiple operating systems

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/shaikabida617/blink-remainder-system.git
2. Navigate to the Project Directory
cd blink-remainder-system
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment

For Windows PowerShell:

venv\Scripts\Activate.ps1
5. Install Required Dependencies
pip install -r requirements.txt
6. Run the Project
python main.py
7. Stop the Application

To stop the application, press:

Q


**Important:** Your actual GitHub repository is **`blink-remainder-system`** (with **remainder**), so use this exact URL:
:contentReference[oaicite:0]{index=0}

Author:

Shaik Abida

GitHub: https://github.com/shaikabida617
