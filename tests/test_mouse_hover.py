from playwright.sync_api import sync_playwright

def test_mouse_hover(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("//button[text()='Point Me']").hover()
    page.wait_for_timeout(2000)
    page.locator("//a[text()='Laptops']").hover()
    page.wait_for_timeout(2000)