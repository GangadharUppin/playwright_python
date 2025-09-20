from playwright.sync_api import sync_playwright

def test_frame(page):
    page.goto("https://vinothqaacademy.com/iframe/")
    frame_page = page.frame_locator("//iframe[@name='popuppage']")
    frame_page.locator("text=Alert Box").nth(1).click()
    page.wait_for_timeout(6000)

