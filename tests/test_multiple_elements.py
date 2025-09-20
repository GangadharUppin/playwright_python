from playwright.sync_api import sync_playwright

def test_multiple_elements(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    elements = page.locator("//a").all()
    print(f'elements : {len(elements)}')
    for ele in elements:
        print(f'ele on text: {ele.inner_text()}')
