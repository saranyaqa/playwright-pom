# pages/base_page.py
import time

from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.click(locator)

    def fill(self, locator: str, value: str):
        self.page.fill(locator, value)

    def get_text(self, locator: str):
        return self.page.inner_text(locator)

    def fill_text_field(self, locator: str, value: str, timeout: int = 3000,  delay: int = 50):
        field = self.page.locator(locator)
        field.wait_for(state="visible")
        field.focus()
        time.sleep(1)
        # Then check manually if it's enabled
        assert field.is_enabled()
        field.fill("")  # Clear any existing text
        field.type(value, delay=delay)


