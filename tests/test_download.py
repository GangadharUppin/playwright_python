from playwright.sync_api import sync_playwright

def xtest_download_file_good(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("//a[text()='Download Files']").click()
    page.wait_for_timeout(2000)
    page.locator("//button[text()='Generate and Download PDF File']").click()
    page.wait_for_timeout(2000)
    page.locator("//button[text()='Download PDF File']").click()
    page.wait_for_timeout(2000)
    page.wait_for_timeout(2000)


