*** Settings ***
Documentation     My first robot framework
Library           SeleniumLibrary

*** Variables ***
${options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()
${URL}        https://www.saucedemo.com/
${BROWSER}    firefox
${USERNAME}   standard_user
${PASSWORD}   secret_sauce
${USERNAME-INVALID}  test123
${PASSWORD-INVALID}   test
@{PRODUCTS}         sauce-labs-backpack    sauce-labs-bike-light    sauce-labs-bolt-t-shirt
@{PRODUCT_NAMES}    Sauce Labs Backpack    Sauce Labs Bike Light    Sauce Labs Bolt T-Shirt



*** Test Cases ***
Login With Valid Credentials
    Login and verify with Valid Credentials keyword
Login With Invalid Credentials
    Login and verify with Invalid Credentials keyword
Login With Valid Credentials Add a product and verify the product is added in cart
    Login and verify with Valid Credentials Add a product to cart and verify the product is listed keyword
Login and verify with Valid Credentials Add multiple products to cart and proceed to checkout and verify the quantities in checkout
    Login and verify with Valid Credentials Add multiple products to cart and proceed to checkout and verify the quantities in checkout keyword

*** Keywords ***
Login and verify with Valid Credentials keyword
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text      id=user-name    ${USERNAME}
    Input Text      id=password     ${PASSWORD}
    Click Button    id=login-button
    Page Should Contain    Products
    Sleep    2s
    Close Browser
***** Keywords ***
login and verify with Invalid Credentials keyword
    Open Browser    ${URL}  ${BROWSER}
    Maximize Browser Window
    Input Text    id=user-name  ${USERNAME-INVALID}
    Input Text    id=password   ${PASSWORD-INVALID}
    Click Button  id=login-button
    Element Should Contain    //*[@id="login_button_container"]/div/form/div[3]/h3  Epic sadface: Username and password do not match any user in this service
    ${error_msg}=    Get Text  //*[@id="login_button_container"]/div/form/div[3]/h3
    Log To Console    Error Message is: ${error_msg}
    Sleep    3s
    Close Browser
***** Keywords ***
Login and verify with Valid Credentials Add a product to cart and verify the product is listed keyword
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text      id=user-name    ${USERNAME}
    Input Text      id=password     ${PASSWORD}
    Click Button    id=login-button
    Click Button    xpath=//button[@id='add-to-cart-sauce-labs-backpack']
    Wait Until Element Is Visible    xpath=//a[@class='shopping_cart_link']    5s
    Click Element    xpath=//a[@class='shopping_cart_link']
    Page Should Contain    Sauce Labs Backpack
    Sleep    3s
    Close Browser

...*** Keywords ***
Login and verify with Valid Credentials Add multiple products to cart and proceed to checkout and verify the quantities in checkout keyword
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

    #  Login
    Input Text      id=user-name    ${USERNAME}
    Input Text      id=password     ${PASSWORD}
    Click Button    id=login-button


     # Handle alert after login in

#    Call Method    ${options}    add_argument    --disable-save-password-bubble
#    Call Method    ${options}    add_argument    --disable-info-bars

    Run Keyword And Ignore Error    Handle Alert    action=ACCEPT
    Page Should Contain    Products


    # Add Multiple Products
    FOR    ${product}    IN    @{PRODUCTS}
        Wait Until Element Is Visible    id=add-to-cart-${product}    10s
        Click Button    id=add-to-cart-${product}
    END

    # Go To Cart
    Click Element    xpath=//a[@class='shopping_cart_link']

    #  Verify Products In Cart
    FOR    ${name}    IN    @{PRODUCT_NAMES}
    Page Should Contain Element    xpath=//div[text()='${name}']
    END

    #  Proceed To Checkout
    Click Button    id=checkout

    # Fill Checkout Details
    Input Text    id=first-name    John
    Input Text    id=last-name     Doe
    Input Text    id=postal-code   600001
    Click Button  id=continue

    # Verify Checkout Summary
    FOR    ${product}    IN    @{PRODUCTS}
        Page Should Contain Element    xpath=//div[@class='inventory_item_name' and contains(text(),'Sauce Labs Backpack')]
    END

    # ✅ Verify Quantity
    ${count}=    Get Element Count    xpath=//div[@class='cart_quantity' and text()='1']
    Should Be Equal As Integers    ${count}    3

    Close Browser