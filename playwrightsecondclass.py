from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # driver = webdriver.firefox()
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").dblclick()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()