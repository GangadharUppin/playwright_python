from playwright.sync_api import sync_playwright

def test_dd(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # page.get_by_test_id('country').click()
    page.locator("//select[@id='country']").select_option(value="india")
    page.wait_for_timeout(2000)
    page.locator("//select[@id='country']").select_option(index=2)
    page.wait_for_timeout(2000)
    page.locator("//select[@id='country']").select_option("India")
    page.wait_for_timeout(2000)

    values = page.locator("//select[@id='country']/child::option").all_inner_texts()
    print(f'Values in drop down: {values}')

    values = page.locator("//select[@id='country']/child::option").all()
    for i in  values:
        print(f'Value is: {i.inner_text().strip()}')

def test_value_from_attribute(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    values = page.locator("//select[@id='country']/child::option").all()
    for i in values:
        print(f'value attribue value: {i.get_attribute('value')}')


