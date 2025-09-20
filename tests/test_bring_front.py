from playwright.sync_api import sync_playwright


def test_bring_front():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://demo.automationtesting.in/Windows.html")

        with page.expect_popup() as popup_info:
            page.locator("//a[text()='Open Seperate Multiple Windows']").click()
            page.locator("//button[@onclick='multiwindow()']").click()

        pop_up = popup_info.value
        pop_up.bring_to_front()
        page.wait_for_timeout(2000)
        print(f'pop up is : {pop_up}')




