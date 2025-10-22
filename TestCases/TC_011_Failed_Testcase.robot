*** Settings ***
Library  SeleniumLibrary
Library  String
Library  ../TestBase/BaseClass.py
Library  ../PageObjects/HomePage.py
Library  ../PageObjects/LoginPage.py
Library    ../Utils/ScreenshotListener.py

Test Setup        Open Application
Test Teardown    Run Keywords    Capture Screenshot On Failure    AND    Close Browser

*** Variables ***
${URL}
${BROWSER}


*** Test Cases ***
User Login In
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