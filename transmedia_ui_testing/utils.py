import allure
import json


@allure.step("Take a screenshot and attach it to Allure report")
def take_screenshot(page, step_name):
    """Capture a screenshot and attach it to the Allure report."""
    screenshot = page.screenshot()
    allure.attach(screenshot, name=step_name, attachment_type=allure.attachment_type.PNG)