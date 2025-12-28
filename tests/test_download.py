import os

from playwright.sync_api import sync_playwright

def test_download_file_good(page):
    page.goto("https://www.selenium.dev/")
    page.locator("//span[text()='Downloads']").click()
    page.wait_for_timeout(2000)
    # page.locator("//button[text()='Generate and Download PDF File']").click()
    # page.wait_for_timeout(2000)
    with page.expect_download() as download_info:
        page.locator("//a[text()='4.35.0']").click()
        page.wait_for_timeout(2000)
    download = download_info.value
    download.save_as(r"C:\Users\ACER\Desktop\Learning\playwright_python\downloads\selenium.jar")
