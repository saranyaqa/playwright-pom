
from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):

    def navigate_to_login(self, url):
        self.navigate(url)

    def enter_email(self, email: str):
        self.fill_text_field(LoginPageLocators.USERNAME_FIELD, email)

    def enter_password(self, password: str):
        self.fill_text_field(LoginPageLocators.PASSWORD_FIELD, password)

    def click_sign_in(self):
        self.click(LoginPageLocators.SIGN_IN_BUTTON)


