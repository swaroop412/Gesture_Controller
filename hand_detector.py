import cv2
import mediapipe as mp
# Explicitly import the 'hands' solution
from mediapipe.python.solutions import hands as mp_hands

class HandDetector:
    def __init__(self, max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7):
        # Use the imported mp_hands
        self.hands = mp_hands.Hands(
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def process_frame(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.hands.process(rgb)

    def draw_landmarks(self, frame, hand_landmarks):
        h, w, _ = frame.shape
        # Draw connections
        # Use mp_hands.HAND_CONNECTIONS
        for connection in mp_hands.HAND_CONNECTIONS:
            start_idx = connection[0]
            end_idx = connection[1]
            start_pt = hand_landmarks.landmark[start_idx]
            end_pt = hand_landmarks.landmark[end_idx]
            cv2.line(frame, (int(start_pt.x * w), int(start_pt.y * h)), (int(end_pt.x * w), int(end_pt.y * h)), (255, 255, 255), 2)
        # Draw landmarks
        for lm in hand_landmarks.landmark:
            cv2.circle(frame, (int(lm.x * w), int(lm.y * h)), 5, (255, 0, 255), cv2.FILLED)