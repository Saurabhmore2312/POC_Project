*** Settings ***
Library    SeleniumLibrary
Library    String
Library    ../TestBase/BaseClass.py
Library    ../PageObjects/HomePage.py
Library    ../PageObjects/AccountRegisterPage.py

Test Setup        Open Application
Test Teardown     Close Browser

*** Variables ***
${URL}
${BROWSER}

*** Test Cases ***
User Registration With Random Data
    Generate Test Data
    Title Should Be         Your Store
    Click Account
    Sleep    2s
    Click Register
    Enter Firstname        ${USERNAME}
    Enter Lastname         ${LASTNAME}
    Enter Email            ${EMAIL}
    Enter Phone Number     ${PHONE}
    Enter Password         ${PASSWORD}
    Enter Cfm Password     ${PASSWORD}
    Click Agree
    Click Continue
    ${msg}=    Get Confirmation Message
    Should Be Equal    ${msg}    Your Account Has Been Created!

*** Keywords ***
Open Application
    ${URL}=       Fetch Property    appURL
    ${BROWSER}=   Fetch Property    browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    3s

Generate Test Data
    ${USERNAME}=    Generate Random String    8    [LETTERS]
    ${LASTNAME}=    Generate Random String    6    [LETTERS]
    ${RAND_EMAIL}=  Generate Random String    6    [LETTERS]
    ${EMAIL}=       Set Variable    ${USERNAME}_${RAND_EMAIL}@example.com
    ${PASSWORD}=    Generate Random String    10    [LETTERS][NUMBERS]
    ${PHONE}=       Generate Random String    10    [NUMBERS]
    Set Test Variable    ${USERNAME}
    Set Test Variable    ${LASTNAME}
    Set Test Variable    ${EMAIL}
    Set Test Variable    ${PASSWORD}
    Set Test Variable    ${PHONE}
