from Sauclabsdemowebsiitetask import Openurl


def test_getbrowserpageinfo():
    url = 'https://www.saucedemo.com/'
    browser = Openurl(url)
    browser.open_website()
    print(browser.fetch_website_title())
    print(browser.fetch_dashboard_title())
    browser.close_browser()