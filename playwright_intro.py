import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="PIM").click()
    page.locator("div:nth-child(3) > .oxd-table-row > div").first.click()
    page.locator("div:nth-child(3) > .oxd-table-row > div:nth-child(9) > .oxd-table-cell-actions > button").first.click()
    page.locator("div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon").click()
  # page.get_by_text("Married").wait_for()
    page.get_by_text("Married").click()
    page.locator("form").filter(has_text="Employee Full NameEmployee").get_by_role("button").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    page.get_by_role("listitem").filter(has_text="mandatest user123").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
