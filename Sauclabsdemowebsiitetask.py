import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Openurl:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def open_website(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def login_with_credentials(self , username, password):
        self.driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='login-button']").click()

    def fetch_url(self):
        self.driver.get(self.url)

    def fetch_website_title(self):
        title = self.driver.title
        print("Website title:", title)
        return title

    def fetch_dashboard_title(self):
        title = self.driver.title
        print("Dashboard title:", title)
        return title


    def close_browser(self):
        self.driver.quit()



