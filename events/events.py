import logging
from pynput import keyboard
import pyperclip
import platform

import sys

sys.path.append("..")

from matlab.matlab import start


FLAG = False

# Detect if the platform is macOS
IS_MAC = platform.system() == "Darwin"

# Define the CONTROL key based on the OS
CONTROL = keyboard.Key.cmd if IS_MAC else keyboard.Key.ctrl

# Define key combinations
current_keys = set()
COMBINATION_CTRL_V = {CONTROL, "v"}
TERMINATE_COMBINATION = {CONTROL, "p"}
COMBINATION_CMD_V_2 = {CONTROL, "v", "1"}
UNDO_KEY = "z"

controller = keyboard.Controller()


def undo():
    global FLAG
    
    FLAG = True  # Set the flag to prevent repeat execution
    
    controller.press(CONTROL)
    controller.press(UNDO_KEY)
    controller.release(UNDO_KEY)
    controller.release(CONTROL)


def show_paste_options():
    # Fetch and print clipboard content
    clipboard_content = pyperclip.paste()
    logging.info(f"Clipboard content: {clipboard_content}")


def on_press(key):
    logging.debug(f"Key pressed: {key}")

    # Handle character keys
    if hasattr(key, "char"):
        # print("went here")
        current_keys.add(key.char)
    else:
        # Handle special keys
        # print("over here")
        current_keys.add(key)
        
    
    if not FLAG:
        # Check for Ctrl+V
        if current_keys == COMBINATION_CTRL_V:
            logging.info("Ctrl+V pressed")
            show_paste_options()

        # Check for Ctrl+V+1
        if current_keys == COMBINATION_CMD_V_2:
            logging.info("Ctrl+V + 1 pressed")
            undo()
            start(pyperclip.paste(), logging)

        # Check for terminating keys (Ctrl+P)
        if current_keys == TERMINATE_COMBINATION:
            logging.info("Ctrl+P pressed. Exiting...")
            return False  # Returning False stops the listener


def on_release(key):
    global FLAG
    logging.info(f"Key released: {key}")
    try:
        # Remove the released key from the current set
        if hasattr(key, "char"):
            current_keys.remove(key.char)
            logging.info(f"Removed {key.char} from current keys")
        else:
            current_keys.remove(key)

        # Reset the flag when the relevant keys are released
        FLAG = False
    except KeyError:
        pass
