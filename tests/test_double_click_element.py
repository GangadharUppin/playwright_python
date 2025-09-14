from playwright.sync_api import sync_playwright

def test_doubleclick(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("//button[text()='Copy Text']").dblclick()
    page.wait_for_timeout(1000)