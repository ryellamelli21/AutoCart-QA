import sys
import os
import pytest

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# --------------------------------
# Project Root Path
# --------------------------------
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, PROJECT_ROOT)


# --------------------------------
# Browser Driver Factory
# --------------------------------
def get_driver(browser):

    # ---------------- CHROME ----------------
    if browser.lower() == "chrome":

        chrome_options = Options()

        # Disable password manager popup
        chrome_options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
        )

        # Browser stability
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-infobars")

        # Faster execution
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")

        # Headless mode (FAST)
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")

        # Extra speed optimizations
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=chrome_options)

    # ---------------- FIREFOX ----------------
    elif browser.lower() == "firefox":

        firefox_options = FirefoxOptions()

        # Headless mode
        firefox_options.add_argument("--headless")

        driver = webdriver.Firefox(options=firefox_options)

        driver.maximize_window()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Faster page loading
    driver.set_page_load_timeout(30)

    # IMPORTANT:
    # Avoid mixing implicit + explicit waits
    driver.implicitly_wait(0)

    return driver


# --------------------------------
# Pytest Fixture
# --------------------------------
@pytest.fixture
def driver(request):

    browser = request.param if hasattr(request, "param") else "chrome"

    driver = get_driver(browser)

    yield driver

    # ---------------- Screenshot on Failure ----------------
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:

        try:
            if driver.session_id:

                if not os.path.exists("screenshots"):
                    os.makedirs("screenshots")

                timestamp = datetime.now().strftime(
                    "%Y-%m-%d_%H-%M-%S"
                )

                screenshot_path = (
                    f"screenshots/"
                    f"{request.node.name}_{timestamp}.png"
                )

                driver.save_screenshot(screenshot_path)

                print(f"\nScreenshot saved: {screenshot_path}")

        except Exception as e:
            print("Screenshot failed:", e)

    # ---------------- Cleanup ----------------
    if driver:
        try:
            driver.quit()
        except Exception:
            pass


# --------------------------------
# Hook to Detect Test Failure
# --------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)