from Sauclabsdemowebsiitetask import Openurl

def test_loginpagesaucelabs():
    url = 'https://www.saucedemo.com'
    browser = Openurl(url)
    browser.open_website()
    print(browser.fetch_url())
    print(browser.login_with_credentials("standard_username", "secret_user"))
    print(browser.fetch_website_title())
    print(browser.fetch_dashboard_title())
    browser.close_browser()



def test_positive_URl_TC_sauce_labs():
    url="https://www.saucedemo.com"
    browser = Openurl(url)
    browser.open_website()
    actual_url = browser.fetch_url()
    expected_url="https://www.saucedemo.com"
    if actual_url==expected_url:
     print("Success, Testing positive_URL_TC_sauce_labs")

def test_negative_URL_TC_sauce_labs():
    url = "https://www.saucedemo.com"
    browser = Openurl(url)
    browser.open_website()
    actual_url = browser.fetch_url()
    expected_url="https://www.testersaucelabs.com"
    if actual_url==expected_url:
     print("Success, Testing negative_URL_TC_sauce_labs")

def test_positive_Website_title_TC_sauce_labs():
    url = "https://www.saucedemo.com"
    browser = Openurl(url)
    browser.open_website()
    actual_title = browser.fetch_website_title()
    expected_title="Swag labs"
    if actual_title==expected_title:
     print("Success, Testing positive_Website_title_TC_sauce_labs")

def test_negative_Website_title_TC_sauce_labs():
    url = "https://www.saucedemo.com"
    browser = Openurl(url)
    browser.open_website()
    actual_title = browser.fetch_website_title()
    expected_title="Swagger"
    if actual_title==expected_title:
     print("Success, Testing negative_Website_title_TC_sauce_labs")

def test_positive_Dashboard_title_TC_sauce_labs():
    url = "https://www.saucedemo.com"
    browser = Openurl(url)
    browser.open_website()
    actual_dashboard_title = browser.fetch_dashboard_title()
    expected_dashboard_title="Swag labs"
    if actual_dashboard_title==expected_dashboard_title:
     print("Success, Testing positive_Dashboard_title_TC_sauce_labs")

def test_negative_Dashboard_title_TC_sauce_labs():
    url = "https://www.saucedemo.com"
    browser = Openurl(url)
    browser.open_website()
    actual_dashboard_title = browser.fetch_dashboard_title()
    expected_dashboard_title="Swagger labs"
    if actual_dashboard_title==expected_dashboard_title:
     print("Success, Testing negative_Dashboard_title_TC_sauce_labs")

