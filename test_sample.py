from playwright.sync_api import Page

def test_playwright_basics(playwright):
    print("✅ Test started inside Docker")
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://nationalpost.com/")
    print("Page title:", page.title())  # logs in Docker terminal
    assert "National Post" in page.title()
    browser.close()

def test_playwright_short_cut(page: Page):
    page.goto("https://nationalpost.com/")
    print("Short cut page title:", page.title())
    assert "National Post" in page.title()
