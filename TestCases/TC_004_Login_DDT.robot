*** Settings ***
Library  SeleniumLibrary
Library  String
Library  ../TestBase/BaseClass.py
Library  ../PageObjects/HomePage.py
Library  ../PageObjects/LoginPage.py

*** Variables ***
${URL}
${BROWSER}

*** Test Cases ***
Login With Multiple Credentials
    [Template]  Perform Login
    user1@xyz.com    Pass@123
    user2@xyz.com    Abc@123
    user3@xyz.com    Test@456

*** Keywords ***
Open Application
    ${URL}  Fetch Property    appURL
    ${BROWSER}  Fetch Property    browser
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window
    Sleep    1s

Perform Login
    [Arguments]    ${email}    ${password}
    Open Application
    Click Account
    Click Login
    Enter Login Email    ${email}
    Enter Login Password    ${password}
    Click Login Button
    Sleep     1s
    Click Account
    Sleep    1s
    Logout Is Visible
    Close Browser
