import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager

class Browser:
    # driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def __init__(self,url):
        self.url = url

    def launch_application(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            return True
        except Exception as e:
            print(f"Error in launching website!!, {e}")
            return False

    def get_title(self):
        if self.launch_application(): # if 2+2 == 4: -> go to if block statement else go to else block statement
            return self.driver.title
        else:
            raise Exception ("Error!!! Page title cannot be found due to browser issue")


    def close_browser(self):
        self.driver.quit() # quit is used for closing all the instances of browser opened by selenium
        # self.driver.close() # close is used for closing latest instances of browser opened by selenium

if __name__ == '__main__':
    url = 'https://www.guvi.in/'
    my_browser = Browser(url)
    title_of_page = my_browser.get_title()
    if title_of_page == 'HCL GUVI | Learn to code in your native language':
        print("Test Passed, Title of page verification completed")
    else:
        print("Test Failed, Title of page verification failed")
    time.sleep(5)
    my_browser.close_browser()