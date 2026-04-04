from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Dashboard:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.implicitly_wait(10)
    def __init__(self):
        self.admin_loc = (By.XPATH,"//span[text()='Admin']")

    def click_admin(self):
        self.driver.find_element(*self.admin_loc).click()