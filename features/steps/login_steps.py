from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('User is able to reach login url')
def open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")


@when('User enters username in the username field "{username}"')
def enter_username(context, username):
    context.driver.find_element(By.ID, "user-name").clear()
    context.driver.find_element(By.ID, "user-name").send_keys(username)


@when('User enters password in the password field "{password}"')
def enter_password(context, password):
    context.driver.find_element(By.ID, "password").clear()
    context.driver.find_element(By.ID, "password").send_keys(password)


@when('User clicks on the login button')
def click_login(context):
    context.driver.find_element(By.ID, "login-button").click()


@then('User should be navigated to the landing page')
def verify_login(context):
    assert "inventory" in context.driver.current_url
    context.driver.quit()