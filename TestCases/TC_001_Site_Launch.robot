*** Settings ***
Library    SeleniumLibrary
Library    ../TestBase/BaseClass.py
Library    ../Utils/ScreenshotListener.py

*** Test Cases ***
Open Browser From Config
    ${URL}=      Fetch Property    appURL
    ${BROWSER}=  Fetch Property    browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    5s
    Title Should Be   Your Store
    Close Browser