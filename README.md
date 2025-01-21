# Autonomous DJI Drone Project

# Overview
This project demonstrates the development of an autonomous DJI drone capable of capturing images, tracking faces, and being controlled via a keyboard interface. Using state-of-the-art technology and the DJI SDK, this project combines computer vision and manual control to showcase versatile drone functionalities.

---

## Features
- **Image Capture:** Automatically or manually capture high-resolution images.
- **Face Tracking:** Utilize computer vision to detect and follow faces in real-time.
- **Keyboard Control:** Control the drone's movement and functionalities with a keyboard interface for precise manual operation.
- **Autonomous Mode:** Switch between manual and autonomous operation modes seamlessly.

---

## Requirements

### Hardware
- DJI Drone (e.g., DJI Mavic, DJI Phantom, or DJI Matrice series)
- Compatible controller for manual operation
- Computer with at least 8GB RAM and a modern processor

### Software
- Python 3.9+
- DJI SDK
- OpenCV
- NumPy
- Keyboard module for Python

### Libraries
Install required libraries via pip:
```bash
pip install dji-sdk opencv-python-headless numpy keyboard
```

---

## Setup

### 1. Install the DJI SDK
Follow the official DJI SDK installation guide for your specific drone model: [DJI SDK Documentation](https://developer.dji.com/documentation/).

### 2. Configure the Drone
1. Connect the drone to your computer.
2. Ensure the drone's firmware is up to date.
3. Set the drone to developer mode via the DJI app.

### 3. Clone the Repository
```bash
git clone https://github.com/kylevitayanuvatti/autonomous_drone.git
cd autonomous_drone
```

### 4. Set Environment Variables
Create a `.env` file and add your DJI SDK keys and credentials:
```plaintext
DJI_APP_KEY=your_app_key
DJI_APP_SECRET=your_app_secret
```

---

## Usage

### 1. Launch the Application
Run the main script:
```bash
python main.py
```

### 2. Keyboard Controls
| Key   | Action                |
|-------|-----------------------|
| W     | Move forward          |
| S     | Move backward         |
| A     | Move left             |
| D     | Move right            |
| Q     | Ascend                |
| E     | Descend               |
| P     | Capture image         |
| T     | Toggle face tracking  |
| M     | Switch mode (manual/autonomous) |

### 3. Autonomous Face Tracking
Press `T` to enable face tracking. The drone will detect and follow any faces within its camera's field of view.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.


---

## Acknowledgments

- [DJI Developers](https://developer.dji.com/) for their robust SDK.
- [OpenCV](https://opencv.org/) for its powerful computer vision tools.
- https://www.computervision.zone for teaching me the basics of DJI Drones and computer vision





