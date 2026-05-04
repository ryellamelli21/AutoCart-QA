from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def close_obstructive_elements(driver):
    possible_elements = [
        (By.ID, "onetrust-accept-btn-handler"),  # cookie popup
        (By.CLASS_NAME, "close"),                # generic modal close
        (By.CSS_SELECTOR, "[data-test='close']"),
    ]

    for by, locator in possible_elements:
        try:
            elem = driver.find_element(by, locator)
            if elem.is_displayed():
                elem.click()
        except NoSuchElementException:
            continue
        except:
            continue