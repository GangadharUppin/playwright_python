import pytest
from playwright.sync_api import sync_playwright
import time


class TestElements:
    @pytest.mark.sanity
    def xtest_locate_element_with_link_text(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False, slow_mo=500)
            page = browser.new_page()
            page.goto("https://playwright.dev/python/")

            # locate a link element with "Docs" text
            docs_btn = page.get_by_role("link", name="Docs")
            docs_btn.click()
            time.sleep(2)
            browser.close()

    def test_get_by_role(self):
        # Search for Products, Brands and More
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False, slow_mo=500)
            page = browser.new_page()
            page.goto("https://www.flipkart.com/")
            time.sleep(2)
            page.get_by_role("textbox", name="Search for Products, Brands").fill("mobiles")
            page.get_by_role("button", name="Search for Products, Brands").click()
            time.sleep(2)
            # page.locator("//a[@title='Cart' and text()='Cart']").click()
            browser.close()