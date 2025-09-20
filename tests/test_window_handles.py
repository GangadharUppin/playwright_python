from playwright.sync_api import sync_playwright


def test_window_handles():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.automationtesting.in/Windows.html")
        page.locator("//a[text()='Open Seperate Multiple Windows']").click()
        page.wait_for_timeout(2000)
        page.locator("//button[@onclick='multiwindow()']").click()
        page.wait_for_timeout(2000)
        no_pages = context.pages
        print(f'no of pages is: {no_pages} {len(no_pages)}')
        page = context.pages[1]
        page.bring_to_front()
        page.wait_for_timeout(2000)
