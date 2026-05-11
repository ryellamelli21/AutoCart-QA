from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import close_obstructive_elements


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        #locators
        self.backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.bike_light_add_button = (By.ID, "add-to-cart-sauce-labs-bike-light")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")
        #Sorting Drop down locator
        self. sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        #First visible product add button after sorting
        self.first_product_add_button = (By.CSS_SELECTOR, ".inventory_item button")
        self.backpack_remove_button = (By.ID, "remove-sauce-labs-backpack")

    def add_backpack_to_cart(self):
        close_obstructive_elements(self.driver)
        self.wait.until(
            EC.visibility_of_element_located(self.backpack_add_button)
        )

        self.wait.until(
            EC.element_to_be_clickable(self.backpack_add_button)
        ).click()

    def add_bike_light_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.bike_light_add_button)
        ).click()

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.cart_icon)
        ).click()

    def get_cart_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.cart_badge)
        ).text

    def remove_backpack_from_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.backpack_remove_button)
        ).click()

    def is_cart_empty(self):
        return len(self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0

    def open_menu(self):
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        ).click()

    def logout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.menu_button)
        ).click()

        self.wait.until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()

    def sort_products_low_to_high(self):
        dropdown = self.wait.until(
            EC.visibility_of_element_located(self.sort_dropdown)
        )

        Select(dropdown).select_by_value("lohi")
    
    def add_first_product_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.first_product_add_button)
        ).click()