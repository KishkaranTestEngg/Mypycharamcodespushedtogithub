*** Settings ***
Documentation     My first robot framework
Library           SeleniumLibrary

*** Test Cases ***
Login Username with Password and check element is visible then logout
    log  "My first testcase"
    Open Browser    https://www.saucedemo.com/       chrome
    Maximize Browser Window
    Input Text    id=user-name    standard_user
    Input Text    id=password    secret_sauce
    Click Element   xpath=//input[@class='submit-button btn_action']
    #Verify Login Successful by clicking item
    Wait Until Element Is Visible    xpath=//span[text()='Products']
    #click the Menu Element to logout
    Click Element    xpath=//button[@id='react-burger-menu-btn']
    #click the logout button
    Wait Until Element Is Visible    xpath= //a[@id='logout_sidebar_link']
    Click Element    xpath=//a[@id='logout_sidebar_link']
    #Confirm after logout came to login page
    Wait Until Element Is Visible   id=login-button
    Page Should Contain Element   id=login-button
    Close Browser