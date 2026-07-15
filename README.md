# Finger Counter CV

## Overview

Finger Counter CV is a real-time computer vision project built with **Python**, **OpenCV**, and **MediaPipe**. The application uses a webcam to detect a hand, track its landmarks, and count the number of raised fingers (0–5).

## Features

- Real-time webcam video processing
- Hand detection and tracking
- Hand landmark visualization
- Counts raised fingers (0–5)
- Displays the finger count on the video feed

## Technologies Used

- Python
- OpenCV
- OpenCV Contrib
- MediaPipe

## Project Structure

```text
Finger Counter CV/
│
├── finger_counter.py      # Main application
└── README.md              # Project documentation
```

## Installation

If you are using a Conda environment, activate it first:

```powershell
conda activate catopencv
```

Install the required libraries:

```powershell
python -m pip install opencv-python
python -m pip install opencv-contrib-python
python -m pip install mediapipe==0.10.21
```

If you are not using Conda, install them with:

```powershell
pip install opencv-python
pip install opencv-contrib-python
pip install mediapipe==0.10.21
```

## Running the Project

Run the application:

```powershell
python finger_counter.py
```

If Python is not configured in your PATH, run it using the full Python path:

```powershell
& "C:\Users\Faris Bahussian\.conda\envs\catopencv\python.exe" finger_counter.py
```

## How It Works

1. Opens the computer webcam.
2. Detects a hand using MediaPipe.
3. Draws the hand landmarks and connections.
4. Determines which fingers are raised.
5. Displays the number of raised fingers in real time.

## Example Output

```text
Fingers: 3
```

The displayed number updates automatically as the user changes their hand gesture.

## Future Improvements

- Hand gesture recognition
- Rock-Paper-Scissors game
- Virtual mouse control
- Volume control using hand gestures
- Air drawing application

## Author

**Faris Bahussain**
