from playwright.sync_api import Page
def test_playwrightBasics(playwright): # playwrite attribute is the global fixture available in pytest_playwright
    browser = playwright.chromium.launch(headless=False) # google chrome , microsoft edge
    context = browser.new_context() # opening an ingonoto window
    page = context.new_page() # open a tab
    page.goto("https://nationalpost.com/") # go to url

# page argument - chromium headless mode default , 1 single context
def test_playwright_short_cut(page:Page):
    page.goto("https://nationalpost.com/")