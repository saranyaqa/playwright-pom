from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.test_data import LOGIN_VALID_USER, URLS, LOGIN_INVALID_USER
import pytest


@pytest.mark.login
def test_login_page(page):
    login_page = LoginPage(page)

    # Navigate to login page
    login_page.navigate_to_login(URLS["login"])

    # Fill credentials robustly
    login_page.enter_email(LOGIN_VALID_USER["username"])
    login_page.enter_password(LOGIN_VALID_USER["password"])

    # Click sign-in safely
    login_page.click_sign_in()

    home_page = HomePage(page)

    # Wait for account icon to ensure page is loaded
    home_page.check_account_icon()

    # Assert using visible text on the homepage as logged user
    assert "My Stuff" in page.content()

@pytest.mark.login
def test_login_page_invalid_password(page):
    pass

