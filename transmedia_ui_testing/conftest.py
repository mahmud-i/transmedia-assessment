import pytest
import json
import os
import shutil
from playwright.sync_api import sync_playwright




def clear_directory(directory):
    """Clear the contents of the given directory."""
    if os.path.exists(directory):
        shutil.rmtree(directory)                                                                        # Remove all files and subdirectories in the directory

    os.makedirs(directory, exist_ok=True)                                                               # Create the directory if it doesn't exist



def pytest_sessionstart(session):
    """Clear or create directories before the test session starts."""
    clear_directory("reports/allure-results")                                                           # directory to store allure results during the session
    clear_directory("reports/allure-report")                                                            # directory to store allure report after the session



@pytest.fixture(scope="session", autouse=True)

def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)                                                     # Launch the Chromium browser
        context = browser.new_context(viewport={"width": 1080, "height": 950})                          # Set the viewport size
        yield context                                                                                   # Return the context
        browser.close()                                                                                 # Close the browser at the end of the session



@pytest.fixture(scope="session", autouse=True)

def load_test_data():
    with open('resources/test_data.json', "r", encoding="utf-8") as file:                               # Open the test data file
        test_data = json.load(file)
    return test_data                                                                                    # Return the test data



def pytest_sessionfinish(session, exitstatus):
    """Generate Allure reports automatically after test run"""
    os.system("allure generate reports/allure-results -o reports/allure-report --clean")                # Generate Allure report
    os.system("allure open reports/allure-report")                                                      # Open Allure report