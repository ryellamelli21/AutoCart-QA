from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        add_btn = wait.until(
            EC.element_to_be_clickable(self.ADD_BACKPACK)
        )
        add_btn.click()

    def get_cart_count(self):
        wait = WebDriverWait(self.driver, 10)
        badge = wait.until(
            EC.presence_of_element_located(self.CART_BADGE)
        )
        return badge.text