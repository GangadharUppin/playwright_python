from playwright.sync_api import sync_playwright

def test_simple_alert(page):

    def handle_dialog(dialog):
        """Handle all types of dialogs."""
        print(f"Dialog type: {dialog.type}")
        print(f"Message: {dialog.message}")
        if dialog.type == "alert":
            dialog.accept()  # Click OK
            print("Alert accepted")
        elif dialog.type == "confirm":
            # To click "Yes"/OK
            dialog.accept()
            # To click "No"/Cancel, use: dialog.dismiss()
            print("Confirm accepted")
        elif dialog.type == "prompt":
            # Provide input text
            dialog.accept("Yes")
            # To cancel, use: dialog.dismiss()
            print("Prompt accepted with input")

    page.on("dialog", handle_dialog)
    page.goto("https://vinothqaacademy.com/alert-and-popup/")
    page.locator("//button[@name='alertbox']").click()
    page.wait_for_timeout(2000)

    page.locator("//button[@name='confirmalertbox']").click()
    page.wait_for_timeout(2000)

    page.locator("//button[@name='promptalertbox1234']").click()
    page.wait_for_timeout(2000)
