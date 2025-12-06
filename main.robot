*** Settings ***    
Library    SeleniumLibrary

*** Test Cases ***
Open Chrome
    Open Browser    https://www.flipkart.com/    chrome
    Maximize Browser Window
    # Title Should Be    Example Domain
    Close Browser