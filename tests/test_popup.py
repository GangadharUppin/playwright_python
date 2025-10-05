from playwright.sync_api import sync_playwright

def test_pop_up(page):
    page.goto("https://webbrowsertools.com/popup-blocker/")


    with page.expect_popup() as popup_info:
        page.locator("//*[@id='popup']/tbody[2]/tr[1]/td[1]/input").click()
        page.wait_for_timeout(2000)
    popup = popup_info.value
    popup.locator("//a[text()='More information...']").click()
    popup.wait_for_timeout(6000)
    popup.close()

def test_wait_for_event(page):
    page.goto("https://webbrowsertools.com/popup-blocker/")
    page.locator("//*[@id='popup']/tbody[2]/tr[1]/td[1]/input").click()
    pop_up = page.wait_for_event("popup")
    pop_up.locator("//a[text()='More information...']").click()
    pop_up.wait_for_timeout(6000)
