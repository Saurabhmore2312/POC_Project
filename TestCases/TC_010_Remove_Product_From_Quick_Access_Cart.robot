*** Settings ***
Library  SeleniumLibrary
Library  String
Library  ../TestBase/BaseClass.py
Library  ../PageObjects/HomePage.py
Library  ../PageObjects/LoginPage.py
Library  ../PageObjects/AddToCartPage.py

Test Setup  Open Application
Test Teardown  Close Browser

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
    Add Iphone To Cart
    Add Macbook To Cart
    Sleep    1s
    Click Quick Access Cart
    Sleep    1s
    Iphone In Quick Access Tab
    Macbook In Quick Access Tab
    Remove Iphone From Quick Access
    Sleep    1s
    Click Quick Access Cart
    Sleep    1s
    Remove Macbook From Quick Access
    Sleep    1s
    Click Quick Access Cart
    Sleep    1s
    Check If Quick Access Cart Is Empty

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