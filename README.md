# Gesture Controlled Smart Remote

A Python-based application that allows you to control your computer's media and screen brightness using hand gestures captured by your webcam.

## Features

Control your system with simple hand gestures:

- **✊ Fist:** Play / Pause media
- **☝ Index Finger:** Volume Up
- **✌ Two Fingers (Index + Middle):** Volume Down
- **🤟 3 Fingers:** Increase Screen Brightness
- **🖖 4 Fingers:** Decrease Screen Brightness
- **🤘 Rock (Index + Pinky):** Forward (Right Arrow)
- **🤙 Pinky:** Backward (Left Arrow)

## Prerequisites

Ensure you have Python installed. You will need the following libraries:

- opencv-python
- mediapipe
- pyautogui
- screen-brightness-control

## Installation

1.  Clone or download this repository.
2.  Install the required dependencies:

    ```bash
    pip install opencv-python mediapipe pyautogui screen-brightness-control
    ```

## Usage

1.  Run the main script:

    ```bash
    python gesture.py
    ```

2.  A window named "Stable Gesture Remote" will open, showing your webcam feed.
3.  Perform gestures in front of the camera to control your system.
4.  Press `Esc` to exit the application.

## Configuration

You can adjust settings in `config.py` such as the hold time for gestures, brightness step size, and camera resolution.