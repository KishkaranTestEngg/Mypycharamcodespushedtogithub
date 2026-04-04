from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



from selenium.webdriver.support.wait import WebDriverWait

# Launch browser
driver = webdriver.Chrome()

# Open website
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

#  Wait until Products page loads (important step)
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))


# Get all product titles
products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

print("Product Titles:")
for product in products:
    print(product.text)

# Logout
menu = driver.find_element(By.ID, "react-burger-menu-btn")
menu.click()

# Now click logout and wait until
wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
# Close browser

driver.quit()