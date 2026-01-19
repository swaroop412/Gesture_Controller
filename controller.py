import pyautogui
import screen_brightness_control as sbc
from config import BRIGHTNESS_STEP

def perform_action(gesture, lm=None):
    if gesture == "FIST":
        pyautogui.press("playpause")

    elif gesture == "INDEX":
        pyautogui.press("volumeup")

    elif gesture == "TWO":
        pyautogui.press("volumedown")

    elif gesture == "THREE":
        try:
            current_brightness = sbc.get_brightness()[0]
        except Exception:
            current_brightness = 50

        new_brightness = min(current_brightness + BRIGHTNESS_STEP, 100)
        sbc.set_brightness(new_brightness)

    elif gesture == "FOUR":
        try:
            current_brightness = sbc.get_brightness()[0]
        except Exception:
            current_brightness = 50

        new_brightness = max(current_brightness - BRIGHTNESS_STEP, 0)
        sbc.set_brightness(new_brightness)

    elif gesture == "ROCK":
        pyautogui.press("right")

    elif gesture == "PINKY":
        pyautogui.press("left")