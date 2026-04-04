from LoginpagePOM import Login
from POM.Invoking_browser import Browser

def test_login_scenario():
    launch_browser = Browser()
    firefox_browser = launch_browser.invoke_browser()
    user_login = Login(firefox_browser)
    user_login.navigate_url()



