from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        #Step One
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

        #step Two
        self.finish_button = (By.ID, "finish")

        #complete Page
        self.success_message = (By.CLASS_NAME, "complete-header")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first_name)

        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)

        self.driver.find_element(*self.continue_button).click()

    def continue_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()
    
    def finish_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()
    
    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success_message)
        ).text
    
    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.error_message)
        ).text