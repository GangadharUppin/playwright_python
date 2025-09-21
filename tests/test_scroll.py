from playwright.sync_api import sync_playwright

def test_scroll(page):
    page.goto("https://automationexercise.com/")
    element = page.locator("//h2[text()='Subscription']")
    #scroll till element found
    element.scroll_into_view_if_needed()
    page.wait_for_timeout(2000)


def test_scroll_down_by_pixels(page):
    page.goto("https://automationexercise.com/")
    page.evaluate("window.scrollBy(0, 500)")
    page.wait_for_timeout(2000)


def test_scroll_up_by_pixels(page):
    page.goto("https://automationexercise.com/")
    page.evaluate("window.scrollBy(0, 500)")
    page.wait_for_timeout(2000)
    page.evaluate("window.scrollBy(0, -500)")
    page.wait_for_timeout(2000)

def test_scroll_till_bottom(page):
    page.goto("https://automationexercise.com/")
    page.evaluate("""
        window.scrollTo(0, document.body.scrollHeight);
    """)
    page.wait_for_timeout(2000)
