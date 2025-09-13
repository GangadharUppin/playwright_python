import pytest
from playwright.sync_api import sync_playwright



@pytest.mark.sanity
def test_open_browser():
    with sync_playwright() as playwright:
        # Launch browser
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        # Create new page
        page = browser.new_page()
        # visit url
        page.goto("https://playwright.dev/python/")
        browser.close()