import pytest
import os
from datetime import datetime
from utils.driver_factory import get_driver


@pytest.fixture
def driver(request):
    driver = get_driver()

    yield driver

    if request.node.rep_call.failed:
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"screenshots/{request.node.name}_{timestamp}.png"

        driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved: {screenshot_name}")
    driver.quit()   

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)