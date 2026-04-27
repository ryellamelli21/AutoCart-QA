import allure
from pages.login_page import LoginPage
from config.config import BASE_URL, USERNAME, PASSWORD
from utils.logger import get_logger

logger = get_logger()


#  VALID LOGIN
@allure.title("Valid Login Test")
@allure.description("Verify user can login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Login Feature")
@allure.story("Valid Login")
def test_valid_login(driver):
    login_page = LoginPage(driver)

    with allure.step("Open login page"):
        login_page.open(BASE_URL)

    with allure.step("Login with valid credentials"):
        login_page.login(USERNAME, PASSWORD)

    with allure.step("Verify successful login"):
        assert login_page.get_page_title() == "Products"


#  INVALID PASSWORD
@allure.title("Invalid Password Test")
@allure.feature("Login Feature")
@allure.story("Invalid Login")
def test_invalid_password(driver):
    login_page = LoginPage(driver)

    with allure.step("Open login page"):
        login_page.open(BASE_URL)

    with allure.step("Login with wrong password"):
        login_page.login(USERNAME, "wrong_password")

    with allure.step("Verify error message"):
        assert "Epic sadface" in login_page.get_error_message()


#  INVALID USERNAME
@allure.title("Invalid Username Test")
@allure.feature("Login Feature")
@allure.story("Invalid Login")
def test_invalid_username(driver):
    login_page = LoginPage(driver)

    with allure.step("Open login page"):
        login_page.open(BASE_URL)

    with allure.step("Login with wrong username"):
        login_page.login("wrong_user", PASSWORD)

    with allure.step("Verify error message"):
        assert "Epic sadface" in login_page.get_error_message()


#  EMPTY CREDENTIALS
@allure.title("Empty Credentials Test")
@allure.feature("Login Feature")
@allure.story("Invalid Login")
def test_empty_credentials(driver):
    login_page = LoginPage(driver)

    with allure.step("Open login page"):
        login_page.open(BASE_URL)

    with allure.step("Login with empty credentials"):
        login_page.login("", "")

    with allure.step("Verify error message"):
        assert "Epic sadface" in login_page.get_error_message()