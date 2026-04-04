*** Settings ***
Documentation     My first robot framework
Library           SeleniumLibrary

*** Variables ***
${URL}        https://www.saucedemo.com/
${BROWSER}    chrome
${USERNAME}   standard_user
${PASSWORD}   secret_sauce

*** Test Cases ***
    Test case 1 Verify Valid Credentials With Correct Username And Password
    login and verify with valid Credentials

*** Keywords ***
login and verify with valid Credentials
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text      id=user-name    ${USERNAME}
    Input Text      id=password     ${PASSWORD}
    Click Button    id=login-button
    Page Should Contain    Products
    Sleep    2s
    Close Browser