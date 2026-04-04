import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/tables.html')
time.sleep(2)


tableselect= driver.find_elements(By.XPATH,"//table[@class='sortable']/tbody/tr/td")
for each_tableselect in tableselect:
    print(each_tableselect.text)
driver.quit()