from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.continue_shopping_button = (By.ID, "continue-shopping")

    def checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()
    
    def get_cart_items_count(self):
        return len(
            self.wait.until(
                EC.presence_of_all_elements_located(self.cart_items)
            )
        )
    def continue_shopping(self):
        self.wait.until(
            EC.element_to_be_clickable(self.continue_shopping_button)
        ).click()
        