import pytest
import allure
from pages.login_page import LoginPage
from config.config import BASE_URL

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
@allure.feature("Advanced login validation")
@allure.story("Password Minimum Length")
def test_password_min_length(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.login("standard_user", "123")

    assert "do not match" in login_page.get_error_message().lower()

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
@allure.feature("Security Validation")
@allure.story("SQL Injection")
def test_sql_injection_login(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.login("' OR '1'='1", "' OR '1'='1")
    assert "Epic sadface" in login_page.get_error_message()

@pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
@allure.feature("Security Validation")
@allure.story("XSS Validation")
def test_xss_driver(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.login("<script>alert('hack')</script>", "password")

    assert "Epic sadface" in login_page.get_error_message()