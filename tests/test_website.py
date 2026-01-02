import selenium
from drivers.driver_setup import create_driver
from pages.login import LoginPage
from pages.common_func import *

def test_website():
    driver = create_driver()
    driver.get("https://www.flipkart.com/")
    driver.save_screenshot(filename="Evidence.png")
    LoginPage.login_scenario(driver)
    privacy_policy(driver)
    terms_of_use(driver)
    driver.back()
    click(driver,element="//*[@alt='Mobiles & Tablets']")
    time.sleep(5)
    click(driver,element="(//*[text()='VIEW ALL'])[1]")
    wait(driver,element="//div[text()='Popularity']")
    driver.close()
    driver.quit()