import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL, USERNAME, PASSWORD

@pytest.mark.parametrize("driver", ["chrome", 'firefox'], indirect=True)
@allure.feature("Extended Cart")
@allure.story("Add Multiple Products")
def test_add_multiple_products(driver):
    login_page =LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()

    assert inventory_page.get_cart_count() == "2"

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
@allure.feature("Extemded Cart")
@allure.story("Remove Story")
def test_remove_product_from_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    inventory_page.add_backpack_to_cart()
    inventory_page.remove_backpack_from_cart()

    assert inventory_page.is_cart_empty()
    