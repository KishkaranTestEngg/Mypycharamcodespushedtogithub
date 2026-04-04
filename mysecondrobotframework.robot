*** Settings ***
Documentation     My second robot framework
Library           SeleniumLibrary

*** Keywords ***
#login page scenario
#    log  "My first testcase"
#    Open Browser    https://www.saucedemo.com/       chrome
#    Maximize Browser Window
#    Input Text    id=user-name    standard_user
#    Input Text    id=password    secret_sauce
#    Click Element   xpath=//input[@class='submit-button btn_action']
#    #Verify Login Successful by clicking item
#    Wait Until Element Is Visible    xpath=//span[text()='Products']
#    #click the Menu Element to logout
#    Click Element    xpath=//button[@id='react-burger-menu-btn']
#    #click the logout button
#    Wait Until Element Is Visible    xpath= //a[@id='logout_sidebar_link']
#    Click Element    xpath=//a[@id='logout_sidebar_link']
#    #Confirm after logout came to login page
#    Wait Until Element Is Visible   id=login-button
#    Page Should Contain Element   id=login-button
#    Close Browser

*** Test Cases ***
login page scenario
#    Login Page Scenario
     Login Username with Password and check element is visible then add to cart and checkout

*** Keywords ***
Login Username with Password and check element is visible then add to cart and checkout
       Log    My first testcase
       Open Browser    https://www.saucedemo.com/    chrome
       Maximize Browser Window

       Input Text    id=user-name    standard_user
       Input Text    id=password    secret_sauce
       Click Button    id=login-button
       # Verify login
       Wait Until Element Is Visible    xpath=//span[text()='Products']

       # Select "Sauce Labs Bike Light"
       Click Element    xpath=//div[text()='Sauce Labs Bike Light']

       # Add to cart
       Click Button    xpath=//button[text()='Add to cart']

       # Go to cart
       Click Element    xpath=//a[@class='shopping_cart_link']

       # Checkout
       Click Button    id=checkout

       Input Text    id=first-name    kishore
       Input Text    id=last-name     karan
       Input Text    id=postal-code   6000024

       Click Button    id=continue
       Click Button    id=finish

       # Verify success
       Element Should Contain    xpath=//h2    Thank you for your order!

       Close Browser
