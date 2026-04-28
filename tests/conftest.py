import pytest
import os
from datetime import datetime

from utils.driver_factory import get_driver


@pytest.fixture
def driver(request):
    browser = request.param if hasattr(request, "param") else "chrome"

    driver = get_driver(browser)

    yield driver

    # Screenshot on failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            if driver.session_id:  # check if session is alive
                if not os.path.exists("screenshots"):
                    os.makedirs("screenshots")

                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                path = f"screenshots/{request.node.name}_{timestamp}.png"
                driver.save_screenshot(path)
        except Exception as e:
            print("Screenshot failed:", e)

    if driver:
        driver.quit()


# Hook to detect test failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)