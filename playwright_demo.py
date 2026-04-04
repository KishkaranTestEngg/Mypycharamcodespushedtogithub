from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False) # driver = webdriver.firefox()
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.locator("[name='username']").fill('Admin') # driver.find_element(By.locator_addrss).send_keys()
    page.locator("[name='password']").fill('admin123')
    page.locator("[type='submit']").click()
    print(page.title())
    print(page.url)
    page.get_by_role("link", name="PIM").click()
    page.evaluate("window.scrollBy(0,300)")
    page.locator("div:nth-child(3) > .oxd-table-row > div").first.click()
    page.locator(
        "div:nth-child(3) > .oxd-table-row > div:nth-child(9) > .oxd-table-cell-actions > button").first.click()
    page.locator(
        "div:nth-child(2) > .oxd-input-group > div:nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon").click()
    # page.get_by_text("Married").wait_for()
    page.get_by_text("Married").click()
    page.locator("form").filter(has_text="Employee Full NameEmployee").get_by_role("button").click()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
    page.get_by_role("listitem").filter(has_text="mandatest user123").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()
    page.close()
    browser.close()