import logging
from events.events import on_press, on_release
from pynput import keyboard

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    logging.info(
        "Script started. Listening for Ctrl+V and Ctrl+C. Press Ctrl+C to stop."
    )

    # Set up the keyboard listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    logging.info("Starting main function...")
    main()
    logging.info("Script ended.")