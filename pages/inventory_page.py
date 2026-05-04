from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import close_obstructive_elements


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_backpack_to_cart(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_button.click()

    def get_cart_count(self):
        cart_badge = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        return cart_badge.text

    def remove_backpack_from_cart(self):
        close_obstructive_elements(self.driver)
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
        ).click()

    def get_cart_count(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        ).text

    def is_cart_empty(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0

    def go_to_cart(self):
        close_obstructive_elements(self.driver)
        self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

    def open_menu(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        ).click()

    def logout(self):
        close_obstructive_elements(self.driver)
        self.open_menu()

        self.wait.until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        ).click()

    def add_bike_light_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))
        ).click()