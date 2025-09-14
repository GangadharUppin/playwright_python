from playwright.sync_api import sync_playwright


def test_upload_file(page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("//input[@id='singleFileInput']").set_input_files(r"C:\Users\ACER\Downloads\Jenkins_Interview_Prep_SDET.pdf")
    print('file is uploaded ....')
    page.wait_for_timeout(2000)
    page.locator("//input[@id='multipleFilesInput']").set_input_files([r"C:\Users\ACER\Downloads\Jenkins_Interview_Prep_SDET.pdf"
                                                                   , r"C:\Users\ACER\Desktop\Learning\playwright_python\tests\test_mouse_hover.py"])
    print('file is uploaded ....')
    page.wait_for_timeout(2000)
