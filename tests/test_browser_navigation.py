from playwright.sync_api import sync_playwright

def test_navigation(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.get_by_role('link', name='Blog').nth(1).click()
    page.reload()
    page.wait_for_timeout(2000)
    page.go_back()
    page.wait_for_timeout(2000)
    page.go_forward()
    page.wait_for_timeout(2000)

