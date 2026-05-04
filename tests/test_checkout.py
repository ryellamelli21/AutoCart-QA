import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import BASE_URL, USERNAME, PASSWORD

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
@allure.feature("Checkout")
@allure.story("Successful Checkout")
def test_successful_checkout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page.checkout()

    checkout_page.fill_checkout_info("Rahul", "Y", "500001")
    checkout_page.finish_checkout()

    assert "Thank you for your order!" in checkout_page.get_success_message()

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
@allure.feature("Checkout")
@allure.story("Empty CHeckout Fields")
def test_checkout_empty_fields(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page.checkout()

    checkout_page.fill_checkout_info("", "", "")
    checkout_page.continue_checkout()

    assert "Error" in checkout_page.get_error_message()