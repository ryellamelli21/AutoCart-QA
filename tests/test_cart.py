from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL, USERNAME, PASSWORD

def test_add_product_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_count() == "1"