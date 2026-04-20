from selenium.webdriver.common.by import By

class InventoryPage:
    ADD_TO_CART_BUTTON =  (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
    
    def add_backpack_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
    
    def get_cart_count(self):
        return self.driver.find_element(*self.CART_BADGE).text