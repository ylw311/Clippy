import logging
from pynput import keyboard
import pyperclip
import platform

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Detect if the platform is macOS
IS_MAC = platform.system() == 'Darwin'

# Define the CONTROL key based on the OS
CONTROL = keyboard.Key.cmd if IS_MAC else keyboard.Key.ctrl

# Define key combinations
current_keys = set()
COMBINATION_CTRL_V = {CONTROL, 'v'}
TERMINATE_COMBINATION = {CONTROL, 'p'}  # Changed to Ctrl+P for termination

def show_paste_options():
    # Fetch and print clipboard content
    clipboard_content = pyperclip.paste()
    logging.info(f"Clipboard content: {clipboard_content}")

def on_press(key):
    logging.debug(f"Key pressed: {key}")
    
    # Handle character keys
    if hasattr(key, 'char'):
        print("went here")
        current_keys.add(key.char)
    else:
        # Handle special keys
        print("over here")
        current_keys.add(key)

    # Check for Ctrl+V
    if CONTROL in current_keys and 'v' in current_keys:
        logging.info('Ctrl+V pressed')
        show_paste_options()
    
    # Check for terminating keys (Ctrl+P)
    if CONTROL in current_keys and 'p' in current_keys:
        logging.info('Ctrl+P pressed. Exiting...')
        return False  # Returning False stops the listener

def on_release(key):
    logging.debug(f"Key released: {key}")
    try:
        # Remove the released key from the current set
        if hasattr(key, 'char'):
            current_keys.remove(key.char)
        else:
            current_keys.remove(key)
    except KeyError:
        pass