import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Guvilogincheck:
    def __init__(self,URL):
        self.URL = URL
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def check_url(self,url):
        self.driver.get(url)
        print("URL is:", url)
        self.driver.maximize_window()

    def login_page_navigate_sign_up_page(self):
       self.driver.find_element(By.ID, "login-btn").click()
       time.sleep(2)
       print("Navigated to sign_up page after login page",self.driver.current_url)

    def sign_up_page_enter_credentials(self):
        self.driver.find_element(By.ID, "email").send_keys("kishkaranptestengineer@gmail.com")
        self.driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Kishore@123")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//a[@id='login-btn']").click()

    def after_login_close_browser(self):
        self.driver.close()
