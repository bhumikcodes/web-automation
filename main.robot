*** Settings ***    
Library    SeleniumLibrary

*** Test Cases ***
Open Chrome
    Open Browser    https://www.flipkart.com/    chrome
    Maximize Browser Window
    Log To Console    message=Passed
    # Title Should Be    Example Domain
    Close Browser