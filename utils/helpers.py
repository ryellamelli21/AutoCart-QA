from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def close_obstructive_elements(driver):
    possible_elements = [
        (By.ID, "onetrust-accept-btn-handler"), #cookie popup
        (By.CLASS_NAME, "close"),
        (By.CSS_SELECTOR, "[data-test='close']"),
        (By.CSS_SELECTOR, ".modal-footer-button"),
        (By.CSS_SELECTOR, ".popup-close"),
    ]

    for by, locator in possible_elements:
        try:
            elem =driver.find_element(by, locator)
            if elem.is_displayed():
                elem.click()
                time.sleep(1)
        except NoSuchElementException:
            continue
        except Exception:
            continue

def safe_click(driver, locator, timeout=20):
    """
    Click element safely after closing obstructions.
    """
    close_obstructive_elements(driver)

    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    element.click()

def safe_send_keys(driver, locator, text, timeout=10):
    """
    Send keys safely after ensuring visibility
    """

    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )
    element.clear()
    element.send_keys(text)