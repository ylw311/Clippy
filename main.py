import logging
from events.events import setup_hotkeys
import keyboard

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Script started. Listening for Ctrl+V and Ctrl+P. Press Ctrl+P to stop.")
    setup_hotkeys()

    try:
        # Block forever, listening for hotkeys
        logging.info("Waiting for hotkey actions...")
        keyboard.wait()  
    except KeyboardInterrupt:
        logging.info("Script interrupted manually with Ctrl+C.")

if __name__ == '__main__':
    logging.info("Starting main function...")
    main()
    logging.info("Script ended.")
