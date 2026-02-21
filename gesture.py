"""
Gesture Controlled Smart Remote (ADB Android Version)

Gestures:
✊ Fist           → Play / Pause (ADB 85)
☝ Index only     → Volume Up (ADB 24)
✌ Index + Middle → Volume Down (ADB 25)
3 Fingers        → Brightness Up (ADB 221)
4 Fingers        → Brightness Down (ADB 220)
🤘 Rock           → Forward (ADB 22)
🤙 Pinky          → Backward (ADB 21)
"""

import sys
from unittest.mock import MagicMock
# Mock matplotlib to prevent errors since it is excluded from the build
sys.modules["matplotlib"] = MagicMock()
sys.modules["matplotlib.pyplot"] = MagicMock()
sys.modules["matplotlib.animation"] = MagicMock()

import cv2
import time
from config import HOLD_TIME, CAMERA_WIDTH, CAMERA_HEIGHT
from hand_detector import HandDetector
from gesture_recognizer import detect_gesture
from controller import perform_action

def main():
    # ---------------- CAMERA ----------------
    cap = cv2.VideoCapture(0)
    cap.set(3, CAMERA_WIDTH)
    cap.set(4, CAMERA_HEIGHT)

    # ---------------- HAND DETECTOR ----------------
    detector = HandDetector()

    # ---------------- TIMERS ----------------
    last_gesture = None
    gesture_start = 0

    # ---------------- MAIN LOOP ----------------
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        result = detector.process_frame(frame)

        now = time.time()

        if result.multi_hand_landmarks:
            hand = result.multi_hand_landmarks[0]
            lm = hand.landmark
            detector.draw_landmarks(frame, hand)

            gesture = detect_gesture(lm)

            if gesture != last_gesture:
                last_gesture = gesture
                gesture_start = now

            elif gesture and now - gesture_start > HOLD_TIME:
                perform_action(gesture, lm)
                gesture_start = now  # reset hold timer

            if gesture:
                cv2.putText(frame, f"Gesture: {gesture}",
                            (20, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 3)

        cv2.imshow("Stable Gesture Remote", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()