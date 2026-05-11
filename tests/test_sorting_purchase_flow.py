import pytest
import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import BASE_URL, USERNAME, PASSWORD

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
@allure.feature("Sorting Purchase Flow")
@allure.story("Sort Low to High + Purchase Cheapest")
def test_sorting_purchase_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    inventory_page.sort_products_low_to_high()

    inventory_page.add_first_product_to_cart()

    inventory_page.go_to_cart()

    cart_page.checkout()

    checkout_page.fill_checkout_info("Rahul", "Sorting", "500001")
    checkout_page.finish_checkout()

    assert "Thank you for your order!" in checkout_page.get_success_message()