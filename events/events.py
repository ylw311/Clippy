import logging
import pyperclip
import keyboard
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def show_paste_options():
    # Fetch and print clipboard content
    # clipboard_content = pyperclip.paste()
    # logging.info(f"Clipboard content: {clipboard_content}")
    logging.info(f"Clipboard content: paste some stuff here :)")


def setup_hotkeys():
    # Add hotkey for Ctrl+V
    try:
        keyboard.add_hotkey('ctrl+v', lambda: (logging.info('Ctrl+V pressed'), show_paste_options()))
        logging.debug("Hotkey Ctrl+V set up successfully.")
    except Exception as e:
        logging.error(f"Failed to set up Ctrl+V: {e}")

    # Add hotkey for Ctrl+P to stop the script
    try:
        keyboard.add_hotkey('ctrl+p', lambda: (logging.info('Ctrl+P pressed. Exiting...'), os._exit(0)))
        logging.debug("Hotkey Ctrl+P set up successfully.")
    except Exception as e:
        logging.error(f"Failed to set up Ctrl+P: {e}")
