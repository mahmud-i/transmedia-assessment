import pytest
import json
import os
import shutil
from playwright.sync_api import sync_playwright


def clear_directory(directory):
    """Clear the contents of the given directory."""
    if os.path.exists(directory):
        # Remove all files and subdirectories in the directory
        shutil.rmtree(directory)
    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)


def pytest_sessionstart(session):
    """Clear or create directories before the test session starts."""
    clear_directory("reports/allure-results")
    clear_directory("reports/allure-report")



@pytest.fixture(scope="session", autouse=True)
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1080, "height": 950})
        yield context
        browser.close()

@pytest.fixture(scope="session", autouse=True)
def load_test_data():
    with open('resources/test_data.json', "r", encoding="utf-8") as file:
        test_data = json.load(file)
    return test_data



def pytest_sessionfinish(session, exitstatus):
    """Generate Allure reports automatically after test run"""
    # Generate Allure report
    os.system("allure generate reports/allure-results -o reports/allure-report --clean")

    # Open Allure report
    os.system("allure open reports/allure-report")