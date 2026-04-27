import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def get_driver(browser="chrome"):
    grid_value = os.environ.get("GRID")
    print(f"GRID ENV VALUE: {grid_value}")

    use_grid = grid_value == "true"

    if use_grid:
        print(f"Running on Selenium Grid with {browser}...")

        if browser == "firefox":
            options = FirefoxOptions()
        else:
            options = ChromeOptions()

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )

    else:
        print(f"Running locally with {browser}...")

        if browser == "firefox":
            options = FirefoxOptions()
            driver = webdriver.Firefox(options=options)
        else:
            options = ChromeOptions()
            driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    return driver