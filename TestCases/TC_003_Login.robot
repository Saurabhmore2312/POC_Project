*** Settings ***
Library  SeleniumLibrary
Library  String
Library  ../TestBase/BaseClass.py
Library  ../PageObjects/HomePage.py
Library  ../PageObjects/LoginPage.py

Test Setup  Open Application
Test Teardown  Close Browser

*** Variables ***
${URL}
${BROWSER}
${USERNAME}
${PASSWORD}


*** Test Cases ***
User Login In
    ${USERNAME}  Fetch Property    username
    ${PASSWORD}  Fetch Property    password
    Click Account
    Sleep    1s
    Click Login
    Enter Login Email  ${USERNAME}
    Enter Login Password  ${PASSWORD}
    Click Login Button
    Sleep    1s
    Click Account
    Sleep    1s
    Logout Is Visible

*** Keywords ***
Open Application
    ${URL}   Fetch Property   appURL
    ${BROWSER}  Fetch Property    browser
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window
    Sleep    1s