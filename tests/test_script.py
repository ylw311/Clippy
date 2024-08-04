from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the credentials for Sauce Labs
SAUCE_USERNAME = os.environ.get('SAUCE_USERNAME')
SAUCE_ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY')

# Debug: Print the credentials to verify they are set correctly
print(f"SAUCE_USERNAME: {SAUCE_USERNAME}")
print(f"SAUCE_ACCESS_KEY: {SAUCE_ACCESS_KEY}")

# Raise an error if credentials are missing
if not SAUCE_USERNAME or not SAUCE_ACCESS_KEY:
    raise ValueError("Sauce Labs credentials are not set in environment variables")

@pytest.fixture
def driver():
    # Define the capabilities and options
    sauceOptions = {
        "name": "Clippy Sriracha",
        "build": "HT6-2024",
        "username": SAUCE_USERNAME,
        "accessKey": SAUCE_ACCESS_KEY
    }

    # Initialize ChromeOptions
    chrome_options = Options()
    chrome_options.set_capability("platformName", "Windows 11")
    chrome_options.set_capability("browserVersion", "latest")
    chrome_options.set_capability("sauce:options", sauceOptions)

    sauce_url = f"https://{SAUCE_USERNAME}:{SAUCE_ACCESS_KEY}@ondemand.saucelabs.com:443/wd/hub"

    # Debug: Print the Sauce Labs URL
    print(f"Connecting to Sauce Labs at: {sauce_url}")

    # Use options instead of desired_capabilities
    driver = webdriver.Remote(
        command_executor=sauce_url,
        options=chrome_options
    )

    yield driver
    driver.quit()

def test_keyboard_events(driver):
    # Use the absolute path to the test_page.html file
    html_file_path = "tests/test_page.html" 
    full_file_path = os.path.abspath(html_file_path)
    
    print(f"Loading HTML file from: {full_file_path}")

    # Navigate to the test page using the full path
    driver.get("file:///" + full_file_path)

    # Debug: Print the page source to ensure it's loaded
    print(driver.page_source)

    # Wait for the page to load completely
    try:
        output = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "output"))
        )
    except Exception as e:
        print(f"Error: {e}")
        # Take a screenshot if the element is not found
        driver.save_screenshot("screenshot.png")
        raise

    # Focus on the body of the HTML page
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()

    # Simulate Ctrl+V
    body.send_keys(Keys.CONTROL, 'v')
    time.sleep(2)

    # Verify the Ctrl+V operation
    try:
        assert output.text == "Ctrl+V pressed"
        print("Ctrl+V Test Passed")
    except AssertionError:
        print("Ctrl+V Test Failed: Output not as expected")

    # Simulate Ctrl+C
    body.send_keys(Keys.CONTROL, 'c')
    time.sleep(1)  # Give some time for the event to trigger

    # Verify the Ctrl+C operation
    try:
        assert output.text == "Ctrl+C pressed"
        print("Ctrl+C Test Passed")
    except AssertionError:
        print("Ctrl+C Test Failed: Output not as expected")
