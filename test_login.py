from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Guvitask11praticewebsite import Guvilogincheck

def test_functionalties_GuviWebpage():
 Url="https://www.guvi.in"
 guvitask11 = Guvilogincheck(Url)
 guvitask11.check_url("https://www.guvi.in")
 guvitask11.login_page_navigate_sign_up_page()
 guvitask11.sign_up_page_enter_credentials()
 guvitask11.after_login_close_browser()


def test_positive_URl_TC_GuviWebpage():
    url="https://www.guvi.in"
    browser = Guvilogincheck(url)
    browser.check_url(url)
    actual_url = browser.check_url(url)
    expected_url="https://www.saucedemo.com"
    if actual_url==expected_url:
     print("Success, Testing positive_URL_TC_Guvi_login_check")

def test_negative_URl_TC_GuviWebpage():
    url="https://www.guvi.in"
    browser = Guvilogincheck(url)
    browser.check_url(url)
    actual_url = browser.check_url(url)
    expected_url="https://www.testerguvi.com"           
    if actual_url==expected_url:
     print("Success, Testing negative_URL_TC_Guvi_login_check")

def is_username_visible_and_enabled():
    username = self.driver.find_element(By.ID, "email")
    return username.is_displayed() and username.is_enabled()


def is_password_visible_and_enabled():
   password = self.driver.find_element(By.XPATH,"//input[@id='password']" )
   return password.is_displayed() and password .is_enabled()

def is_submit_button_visible_and_enabled(self):
    submit = self.driver.find_element(By.XPATH,"//a[contains(@id,'signup')]")
    return submit.is_displayed() and submit.is_enabled()

def click_submit_button(self):
    wait = WebDriverWait(self.driver, 10)
    submit_btn = (By.XPATH, "//a[contains(@id,'signup')]")
    wait.until(EC.element_to_be_clickable(submit_btn)).click()
