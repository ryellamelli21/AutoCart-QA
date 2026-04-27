from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL, USERNAME, PASSWORD
import time

def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page  = InventoryPage(driver)

    login_page.open(BASE_URL)
    time.sleep(3)
    login_page.login(USERNAME, PASSWORD)
    time.sleep(3)
    inventory_page.add_backpack_to_cart()
    time.sleep(5)
    assert inventory_page.get_cart_count() == "1"