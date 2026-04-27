import pytest
import os
from datetime import datetime
from utils.driver_factory import get_driver
import allure 

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    driver = get_driver(browser)
    yield driver

    if request.node.rep_call.failed:
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = f"screenshots/{request.node.name}_{timestamp}.png"

        driver.save_screenshot(screenshot_path)

        # Attach to Allure
        with open(screenshot_path, "rb") as f:
            allure.attach(
                f.read(),
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )

    driver.quit()
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)