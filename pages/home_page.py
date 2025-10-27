from pages.locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):
    def check_account_icon(self):
        self.page.wait_for_selector(HomePageLocators.ACCOUNT_ICON)
        self.page.locator(HomePageLocators.ACCOUNT_ICON)