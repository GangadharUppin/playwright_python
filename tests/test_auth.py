from playwright.sync_api import sync_playwright
from playwright.sync_api import Browser

def xtest_auth(browser: Browser):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel='chrome', headless=False)
        # context = browser.new_context()
        # page = context.new_page()
        context = browser.new_context(
            http_credentials={"username": "admin", "password": "admin"}
        )
        page = context.new_page()
        page.goto("http://the-internet.herokuapp.com/basic_auth")