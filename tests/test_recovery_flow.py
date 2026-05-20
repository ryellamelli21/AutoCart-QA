import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from config.config import BASE_URL, USERNAME, PASSWORD


@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
@allure.feature("Recovery Flow")
@allure.story("Invalid Login Recovery + Purchase")
def test_invalid_login_recovery_purchase(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    #Step 1: Invalid Login
    login_page.open(BASE_URL)
    login_page.login(USERNAME, "wrong_password")

    #Step 2: Validate Error
    assert "Username and password do not match" in login_page.get_error_message()

    #Step 3: Retry valid login
    driver.refresh()
    login_page.clear_fields()
    login_page.login(USERNAME, PASSWORD)

    assert "inventory" in driver.current_url.lower()

    #step 4: Add Product
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    #Step 5: Checkout
    cart_page.checkout()

    #Step 6: Fill Details
    checkout_page.fill_checkout_info("Rahul", "Recovery", "500001")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    #Step 7: Verify Success
    assert "Thank you for your order!" in checkout_page.get_success_message()