from playwright.sync_api import sync_playwright
import pytest

@pytest.mark.create_json
def test_storage_state():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("http://testphp.vulnweb.com/login.php")
        page.locator("//input[@name='uname']").fill("test")
        page.locator("//input[@name='pass']").fill("test")
        page.wait_for_timeout(2000)
        page.locator("//input[@type='submit']").nth(0).click()
        page.wait_for_timeout(2000)
        context.storage_state(path="state.json")
        context.close()
        browser.close()
