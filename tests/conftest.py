import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# -------------------------------
# Browser Driver Factory
# -------------------------------
def get_driver(browser):
    if browser.lower() == "chrome":
        chrome_options = Options()

        # Disable password manager popup
        chrome_options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })

        # Disable browser interruptions
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")

        driver = webdriver.Chrome(options=chrome_options)

    elif browser.lower() == "firefox":
        firefox_options = FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(5)
    return driver


# -------------------------------
# Pytest Fixture
# -------------------------------
@pytest.fixture
def driver(request):
    browser = request.param if hasattr(request, "param") else "chrome"

    driver = get_driver(browser)

    yield driver

    # Screenshot on failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            if driver.session_id:
                if not os.path.exists("screenshots"):
                    os.makedirs("screenshots")

                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_path = f"screenshots/{request.node.name}_{timestamp}.png"
                driver.save_screenshot(screenshot_path)
                print(f"Screenshot saved: {screenshot_path}")

        except Exception as e:
            print("Screenshot failed:", e)

    # Cleanup
    if driver:
        driver.quit()


# -------------------------------
# Hook to detect test failure
# -------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)