from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope='function')
def page():
    with sync_playwright() as playwright:
        # browser = playwright.chromium.launch(channel='chrome', headless=False)
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        # page.set_viewport_size({'width':1920, 'height':1080})
        yield page
        browser.close()

