import logging
import pyperclip
import platform
import os
from pynput import keyboard

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Detect if the platform is macOS or Windows
IS_MAC = platform.system() == 'Darwin'
IS_WINDOWS = platform.system() == 'Windows'

# Define the CONTROL key based on the OS
CONTROL = keyboard.Key.cmd if IS_MAC else keyboard.Key.ctrl

# Define key combinations
current_keys = set()

CTRL_V_KEYS_WINDOWS = {'\x16'}  # Ctrl+V
CTRL_V1_KEYS_WINDOWS = {'<49>'}  # Ctrl+V+1 using the combined representation
CTRL_V2_KEYS_WINDOWS = {'<50>'}  # Ctrl+V+2 using the combined representation
CTRL_V3_KEYS_WINDOWS = {'<51>'}  # Ctrl+V+3 using the combined representation
TERMINATE_COMBINATION_WINDOWS = {'\x10'}  # Ctrl+P (use '\x10' for 'p')

# Define key combinations for macOS
CTRL_V_KEYS_MAC = {keyboard.Key.cmd, 'v'}  # Cmd+V
CTRL_V1_KEYS_MAC = {keyboard.Key.cmd, 'v', '1'}  # Cmd+V+1
TERMINATE_COMBINATION_MAC = {keyboard.Key.cmd, 'p'}  # Cmd+P

def show_paste_options():
    # Fetch and print clipboard content
    clipboard_content = pyperclip.paste()
    logging.info(f"Clipboard content: TESTING")

def on_press(key):
    logging.debug(f"Key pressed: {key}")

    # Handle character keys
    if hasattr(key, "char") and key.char is not None:
        current_keys.add(key.char.lower())  # Use lowercase for consistency
    else:
        # Handle special keys
        current_keys.add(key)  # Ensure special keys are added as actual key objects

    if IS_WINDOWS:
        print('windows')
        # Check for Ctrl+V
        if all(k in current_keys for k in CTRL_V_KEYS_WINDOWS):
            logging.info('Ctrl+V pressed (Windows)')
            show_paste_options()    

        # Check for Ctrl+V+1
        if all(k in current_keys for k in CTRL_V1_KEYS_WINDOWS):
            logging.info('Ctrl+V+1 pressed (Windows)')
            # Handle specific case for Ctrl+V+1
            logging.info('Special key combination Ctrl+V+1 triggered!')
        
        # Check for Ctrl+V+2
        if all(k in current_keys for k in CTRL_V2_KEYS_WINDOWS):
            logging.info('Ctrl+V+2 pressed (Windows)')
            # Handle specific case for Ctrl+V+2
            logging.info('Special key combination Ctrl+V+2 triggered!')

        # Check for Ctrl+V+3
        if all(k in current_keys for k in CTRL_V3_KEYS_WINDOWS):
            logging.info('Ctrl+V+3 pressed (Windows)')
            # Handle specific case for Ctrl+V+3
            logging.info('Special key combination Ctrl+V+3 triggered!')

        # Check for terminating keys (Ctrl+P)
        if all(k in current_keys for k in TERMINATE_COMBINATION_WINDOWS):
            logging.info('Ctrl+P pressed (Windows). Exiting...')
            os._exit(0)  # Terminate the script immediately

    elif IS_MAC:
        print('macOS')
        # Check for Cmd+V
        if all(k in current_keys for k in CTRL_V_KEYS_MAC):
            logging.info('Cmd+V pressed (macOS)')
            show_paste_options()

        # Check for Cmd+V+1
        if all(k in current_keys for k in CTRL_V1_KEYS_MAC):
            logging.info('Cmd+V+1 pressed (macOS)')
            # Handle specific case for Cmd+V+1
            logging.info('Special key combination Cmd+V+1 triggered!')

        # Check for terminating keys (Cmd+P)
        if all(k in current_keys for k in TERMINATE_COMBINATION_MAC):
            logging.info('Cmd+P pressed (macOS). Exiting...')
            os._exit(0)  # Terminate the script immediately

def on_release(key):
    logging.debug(f"Key released: {key}")
    try:
        # Remove the released key from the current set
        if hasattr(key, 'char') and key.char is not None:
            current_keys.remove(key.char.lower())
        else:
            current_keys.remove(key)  # Ensure special keys are removed as key objects
    except KeyError:
        pass

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
