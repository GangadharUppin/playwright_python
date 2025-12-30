import pytest
from playwright.sync_api import sync_playwright
from datetime import datetime



@pytest.mark.normal
def test_open_browser():
    with sync_playwright() as playwright:
        # Launch browser
        browser = playwright.chromium.launch(headless=True, slow_mo=500)
        # Create new page
        page = browser.new_page()
        # visit url
        page.goto("https://playwright.dev/python/")
        print('current time is as')
        print(datetime.now())
        browser.close()

def test_storage_state_json():
    with sync_playwright() as playwright:
        # Launch browser
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state=r"C:\Users\ACER\Desktop\Learning\playwright_python\state.json")
        page = context.new_page()

        page.goto("http://testphp.vulnweb.com/login.php")
        page.wait_for_timeout(8000)
