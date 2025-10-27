from pages.login_page import LoginPage
from pages.home_page import HomePage
from utils.test_data import LOGIN_VALID_USER, URLS
import pytest


@pytest.mark.login
def test_login_page(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login(URLS["login"])
    login_page.enter_email(LOGIN_VALID_USER["username"])
    login_page.enter_password(LOGIN_VALID_USER["password"])
    login_page.click_sign_in()
    home_page = HomePage(page)
    home_page.check_account_icon()
    assert "My Stuff" in page.content()
