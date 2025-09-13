from playwright.sync_api import sync_playwright

def test_right_click_double_click(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("//button[@onclick='toggleButton(this)']").click(button='right')
    page.wait_for_timeout(2000)


def test_dbclick(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("//button[text()='Copy Text']").dblclick()
    page.wait_for_timeout(2000)

