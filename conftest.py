from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope='function')
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

