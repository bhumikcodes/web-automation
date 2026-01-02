*** Settings ***    
Library    SeleniumLibrary
Library    ../bhumikcodes/pages/common_func.py
Library    ../bhumikcodes/drivers/driver_setup.py

*** Test Cases ***
Open Chrome
    Open Browser    https://www.flipkart.com/    chrome
    Maximize Browser Window
    Log To Console    message=Test Passed!
    # Title Should Be    Example Domain
    # Close Browser
