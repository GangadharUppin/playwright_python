from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    browser = pw.chromium.launch(channel='chrome', headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")

    with context.expect_page() as new_page_info:
        page.locator("//button[text()='New Tab']").click()
    new_page = new_page_info.value
    print(f'new page: {new_page}')
    pages = context.pages
    print(f'pages : {pages}')
    new_page.bring_to_front()
    page.wait_for_timeout(10000)
    print(f'new page title : {new_page.title()}')
    print(f'new page title : {new_page.title()}')
