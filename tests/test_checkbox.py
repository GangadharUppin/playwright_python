from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test_checkbox(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("[value='friday']").click()
    page.wait_for_timeout(1000)
    expect(page.locator("[value='friday']")).to_be_checked()
    page.locator("[value='friday']").click()
    page.wait_for_timeout(1000)
    expect(page.locator("[value='friday']")).not_to_be_checked()

