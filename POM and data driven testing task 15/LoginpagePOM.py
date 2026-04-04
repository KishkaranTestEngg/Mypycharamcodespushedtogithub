import time
from fileinput import filename

from selenium.webdriver.common.by import By
from POM.load_userdata import ExcelData


class Login:
    def __init__(self,driver):
        self.driver = driver
        # self.filename = "D:/user_details.xlsx"
        # self.sheetname = 'user_data'
        # self.username_loc = By.NAME,'username' # By.Name,'username' ->(name,username)
        # self.password_loc = (By.NAME,'password')
        # self.login_btn_loc = (By.TAG_NAME,'button')

    def navigate_url(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def login_page(self):
        