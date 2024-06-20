import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser_context():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

def test_login(browser_context):
    page = browser_context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.fill('input[name="username"]', "Admin")
    page.fill('input[name="password"]', "admin123")
    page.click('button[type="submit"]')
    page.close()

def test_logout(browser_context):
    page = browser_context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.fill('input[name="username"]', "Admin")
    page.fill('input[name="password"]', "admin123")
    page.click('button[type="submit"]')
    page.click('p.oxd-userdropdown-name')
    page.click('a.oxd-userdropdown-link[href="/web/index.php/auth/logout"]')
    assert page.is_visible('button[type="submit"]')
    page.close()
