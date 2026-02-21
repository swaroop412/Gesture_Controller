import subprocess

def perform_action(gesture, lm=None):
    """Maps a gesture to an ADB keycode and executes the command directly."""
    gesture_to_keycode = {
        "FIST": "85",   # Play / Pause (KEYCODE_MEDIA_PLAY_PAUSE)
        "INDEX": "24",  # Volume Up (KEYCODE_VOLUME_UP)
        "TWO": "25",    # Volume Down (KEYCODE_VOLUME_DOWN)
        "THREE": "221", # Brightness Up (KEYCODE_BRIGHTNESS_UP)
        "FOUR": "220",  # Brightness Down (KEYCODE_BRIGHTNESS_DOWN)
        "ROCK": "22",
        "PINKY": "21",
    }

    keycode = gesture_to_keycode.get(gesture)
    if keycode:
        # Use the full path to adb.exe
        adb_path = r"C:\Users\Techsupport4\Downloads\platform-tools-latest-windows\platform-tools\adb.exe"
        command = [adb_path, "shell", "input", "keyevent", keycode]
        try:
            subprocess.Popen(command)
        except FileNotFoundError:
            print(f"Error: ADB executable not found at: {adb_path}")