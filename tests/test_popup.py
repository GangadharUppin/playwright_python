from playwright.sync_api import sync_playwright

def xtest_navigation(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("//button[text()='Popup Windows']").click()
    page.wait_for_timeout(5000)
