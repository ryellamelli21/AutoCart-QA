from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    CHECKOUT_COMPLETE = (By.CLASS_NAME, "complete-header")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def fill_checkout_info(self, first_name, last_name, postal_code):

        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)

        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)

        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def continue_checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

    def finish_checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.CHECKOUT_COMPLETE)
        )

    def get_success_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.CHECKOUT_COMPLETE)
        ).text

    def get_error_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text