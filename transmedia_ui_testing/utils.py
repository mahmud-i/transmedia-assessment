import allure


@allure.step("Take a screenshot and attach it to Allure report")
def take_screenshot(page, step_name):
    """Capture a screenshot and attach it to the Allure report."""
    screenshot = page.screenshot()                                                                                    # Take a screenshot of the current page
    allure.attach(screenshot, name=step_name, attachment_type=allure.attachment_type.PNG)                             # Attach the screenshot to the Allure report as an image with the specified name