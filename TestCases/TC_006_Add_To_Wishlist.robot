*** Settings ***
Library  SeleniumLibrary
Library  String
Library  ../TestBase/BaseClass.py
Library  ../PageObjects/HomePage.py
Library  ../PageObjects/LoginPage.py
Library  ../PageObjects/AddToWishlistPage.py
Library    ../Utils/ScreenshotListener.py

Test Setup        Open Application
Test Teardown    Run Keywords    Capture Screenshot On Failure    AND    Close Browser

*** Variables ***
${URL}
${BROWSER}
${USERNAME}
${PASSWORD}


*** Test Cases ***
User Login In
    Peform Login
    Sleep    3s
    Click Logo
    Sleep    1s
    Add Iphone To Wishlist
    Add Macbook To Wishlist
    Click Wishlist
    Sleep    1s
    Iphone Is Visible In Wishlist
    Macbook Is Visible In Wishlist

*** Keywords ***
Open Application
    ${URL}   Fetch Property   appURL
    ${BROWSER}  Fetch Property    browser
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window
    Sleep    1s

Peform Login
    ${USERNAME}  Fetch Property    username
    ${PASSWORD}  Fetch Property    password
    Click Account
    Sleep    1s
    Click Login
    Enter Login Email  ${USERNAME}
    Enter Login Password  ${PASSWORD}
    Click Login Button
    Sleep    1s