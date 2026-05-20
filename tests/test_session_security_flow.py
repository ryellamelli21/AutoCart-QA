import pytest
import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL, USERNAME, PASSWORD

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
@allure.feature("Security Flow")
@allure.story("Session Security Validation")
def test_session_security_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    #Step 1: Login
    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)

    #Step 2: Refresh Browser
    driver.refresh()

    #Step 3: Verify Sessions Persists
    assert "inventory" in driver.current_url

    #Step 4: Logout
    inventory_page.logout()

    #Step 5: Attempt Protected Page Access
    driver.get("https://www.saucedemo.com/inventory.html")

    #Step 6: Verify Redirected
    assert "inventory" not in driver.current_url    