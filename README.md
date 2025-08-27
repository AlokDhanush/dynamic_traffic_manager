# Dynamic Traffic Manager

   A Python-based real-time traffic monitoring system using YOLO and computer vision to perform vehicle detection and counting from live or recorded video.

---

##  Repository Overview
  
  dynamic_traffic_manager/<br>
  ├── real_time_counting.py # Captures video and counts vehicles in real time<br>
  ├── vehicle_counting.py # Performs vehicle detection/counting on recorded footage<br>
  ├── yolov5su.pt # Trained YOLOv5 model weights<br>
  └── Traffic images/ # Sample images or visuals used in development and testing<br>

---

##  Features

- **Real-time Video Analysis**: `real_time_counting.py` can process live video feeds (camera inputs or MP4 files like `cars.mp4`) to detect and count vehicles on the fly.
- **Offline Footage Processing**: `vehicle_counting.py` works on pre-recorded videos, performing vehicle detection without needing a live feed.
- **Custom YOLOv5 Model**: Includes `yolov5su.pt`, a trained model tailored to detect vehicles in your traffic scenarios.
- **Sample Media Assets**: The `Traffic images` directory (and files like `cars.mp4`) helps with testing and visualization.

---

##  Getting Started

### Prerequisites

- Python 3.7 or higher
- Required libraries (likely):
  - `torch`, `torchvision`
  - `opencv-python`
  - `numpy`
  - YOLOv5 dependencies

*(Please verify required packages inside the scripts or your `requirements.txt`, if you have one.)*

### Installation

```bash
git clone https://github.com/AlokDhanush/dynamic_traffic_manager.git
cd dynamic_traffic_manager

# (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # (Linux/macOS) or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt  # if available, otherwise install individually
```

---

Usage
  Real-Time Counting with real_time_counting.py
  
  Starts vehicle counting from a live camera feed or video file:

```bash
 python real_time_counting.py --source path/to/cars.mp4
```
---
Offline Processing with vehicle_counting.py

   Runs detection and counting on existing footage:
```bash
python vehicle_counting.py --video path/to/traffic_video.mp4
```
---


  

  
  
