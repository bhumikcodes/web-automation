import selenium
from drivers.driver_setup import create_driver
from pages.login import LoginPage
from pages.common_func import *
from pages.compare import *

def test_website():
    driver = create_driver()
    driver.implicitly_wait(2)
    driver.get("https://www.flipkart.com/")
    driver.save_screenshot(filename="Evidence.png")
    LoginPage.login_scenario(driver)
    privacy_policy(driver)
    terms_of_use(driver)
    driver.back()
    click(driver,element="//*[@alt='Mobiles & Tablets']")
    wait(driver,element="//a[text()='Corporate Information']")
    click(driver,element="(//*[text()='VIEW ALL'])[1]")
    wait(driver,element="//div[text()='Popularity']")
    ComparePage.OpenLinks(driver)
    driver.close()
    driver.quit()