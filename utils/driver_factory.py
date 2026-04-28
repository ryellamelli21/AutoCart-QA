import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Execution mode:
# local = local machine
# grid = selenium grid/docker
SELENIUM_MODE = os.getenv("SELENIUM_MODE", "local").lower()

GRID_URL = os.getenv("GRID_URL", "http://localhost:4444/wd/hub")


def get_driver(browser):
    browser = browser.lower()

    # ==========================
    # CHROME
    # ==========================
    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")

        if SELENIUM_MODE == "grid":
            driver = webdriver.Remote(
                command_executor=GRID_URL,
                options=chrome_options
            )
        else:
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=chrome_options
            )

    # ==========================
    # FIREFOX
    # ==========================
    elif browser == "firefox":
        firefox_options = webdriver.FirefoxOptions()

        if SELENIUM_MODE == "grid":
            driver = webdriver.Remote(
                command_executor=GRID_URL,
                options=firefox_options
            )
        else:
            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=firefox_options
            )

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(5)
    return driver