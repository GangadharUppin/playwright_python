from playwright.sync_api import sync_playwright


def test_drag_drop(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    source = page.locator("//div[@id='draggable']")
    dest = page.locator("//div[@id='droppable']")
    source_bounding = source.bounding_box()
    page.mouse.move(
        source_bounding['x'] + source_bounding['width']/2,
        source_bounding['y'] + source_bounding['height']/2
    )
    page.mouse.down()
    dest_bounding = dest.bounding_box()
    page.mouse.move(
        dest_bounding['x'] + dest_bounding['width'] /2,
        dest_bounding['y'] + dest_bounding['height'] /2
    )
    page.mouse.up()
    page.wait_for_timeout(1000)
