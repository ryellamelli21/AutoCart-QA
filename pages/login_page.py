from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import safe_click, safe_send_keys, close_obstructive_elements

class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        close_obstructive_elements(self.driver)

        safe_send_keys(self.driver, self.USERNAME_INPUT, username)
        safe_send_keys(self.driver, self.PASSWORD_INPUT, password)

        safe_click(self.driver, self.LOGIN_BUTTON)

    def get_page_title(self):
        return self.driver.find_element(*self.PRODUCTS_TITLE).text
    
    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text
    
    def clear_fields(self):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        )

        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_INPUT)
        )

        username_field.click()
        username_field.clear()

        password_field.click()
        password_field.clear()