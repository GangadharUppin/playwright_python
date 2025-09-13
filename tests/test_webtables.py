from playwright.sync_api import sync_playwright


def test_web_tables(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    num_rows = page.locator("//tbody[@id='rows']/tr").count()
    num_col = page.locator("//tr[@id='headers']/th").count()
    print(f'Number of row and column : {num_rows} {num_col}')

    values_from_tables_is = page.locator("//tbody[@id='rows']/tr/td").all_inner_texts()
    print(f'all the table values: {values_from_tables_is}')
    # print(f'number of values in the table: {len(values_from_tables_is)}')

    