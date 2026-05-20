import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import BASE_URL, USERNAME, PASSWORD


@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect= True)
@allure.feature("End to End Purchase Flow")
@allure.story("Complete User Journey")

def test_complete_user_purchase_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    inventory_page.add_backpack_to_cart()
    inventory_page.add_bike_light_to_cart()
    inventory_page.go_to_cart()

    cart_page.remove_product("Sauce Labs Bike Light")
    cart_page.checkout()

    checkout_page.fill_checkout_info("Rahul", "QA", "534301")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert "Thank you for your order!" in checkout_page.get_success_message()

    inventory_page.logout()