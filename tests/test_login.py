from pages.login_page import LoginPage
from config.config import BASE_URL, USERNAME, PASSWORD
from utils.logger import get_logger

logger = get_logger()

def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)
    logger.info("Opening login page")
    assert login_page.get_page_title() == "Products"
    # assert login_page.get_page_title() == "Wrong"

def test_invalid_password(driver):
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.login(USERNAME, "wrong_password")

    assert "Epic sadface" in login_page.get_error_message()

def test_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.login("wrong_user", PASSWORD)

    assert "Epic sadface" in login_page.get_error_message()

def test_empty_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.login("", "")

    assert "Epic sadface" in login_page.get_error_message()