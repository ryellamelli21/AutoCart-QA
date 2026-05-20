import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL, USERNAME, PASSWORD

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
@allure.feature("Logout")
@allure.story("Valid Logout")
def test_logout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    inventory_page.logout()

    assert "saucedemo" in driver.current_url.lower()