from playwright.sync_api import sync_playwright

#slider-range
def test_sliders(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(2000)
    slider = page.locator("//div[@id='slider-range']")
    bounding_box = slider.bounding_box()
    start_x = bounding_box['x'] + bounding_box["width"] / 2
    start_y = bounding_box["y"] + bounding_box["height"] / 2
    page.mouse.move(start_x , start_y)
    page.mouse.down()
    page.mouse.move(start_x + 900, start_y)
    page.mouse.up()
    page.wait_for_timeout(6000)