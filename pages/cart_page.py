from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import safe_click


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.continue_shopping_button = (By.ID, "continue-shopping")

    def checkout(self):
        safe_click(self.driver, self.checkout_button)

    def remove_product(self, product_name):
        product_ids = {
            "Sauce Labs Backpack" : "remove-sauce-labs-backpack",
            "Sauce Labs Bike Light" : "remove-sauce-labs-bike-light",
            "Sauce Labs Bolt T-Shirt" : "remove-sauce-labs-bolt-t-shirt",
            "Sauce Labs Fleece Jacket" : "remove-sauce-labs-fleece-jacket",
            "Sauce Labs Oneise": "remove-sauce-labs-oneise",
            "Test.allTheThings() T-Shirt (Red)" : "remove-test.allthethings()-t-shirt-(red)"
        }
        if product_name not in product_ids:
            raise ValueError(f"Unknown product: {product_name}")
        
        remove_button = (By.ID, product_ids[product_name])

        self.wait.until(
            EC.element_to_be_clickable(remove_button)
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
