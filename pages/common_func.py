import  selenium
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def terms_of_use(driver):
    # driver= create_driver()
    driver.find_element(By.LINK_TEXT,"Terms of Use").click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    print(driver.title)
    if "Terms" in driver.title:
        print("Term page opened successfully")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return


def privacy_policy(driver):
    # driver= create_driver()
    driver.find_element(By.LINK_TEXT,"Privacy Policy").click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    print(driver.title)
    if "policy" in driver.title:
        print("Privaly policy page opened successfully")
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        return