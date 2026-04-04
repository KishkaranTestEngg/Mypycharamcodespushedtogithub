import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/dropdown.html')
time.sleep(2)

# use of select tag for dropdown menus
# select = Select(driver.find_element(By.TAG_NAME,'select'))
# select.select_by_index(3)
# time.sleep(2)
# select.select_by_value('mercedes')

# Handling radio button with dynamic approach

#driver.find_element(By.XPATH,"//input[@id='cb_red']]").click()

Checkboxes_click = driver.find_elements(By.XPATH,"//label[@for='cb_red']")
for each_checkboxes_click in Checkboxes_click: #[element1,element2,element3]
    each_checkboxes_click.click()
    time.sleep(2)