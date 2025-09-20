from gettext import pgettext

from playwright.sync_api import sync_playwright

def test_key_board(page):
    page.goto("http://testphp.vulnweb.com/login.php")
    page.wait_for_timeout(2000)
    page.keyboard.down("Control")
    page.keyboard.press("A")
    page.wait_for_timeout(2000)