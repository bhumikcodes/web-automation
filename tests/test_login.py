import selenium
from drivers.driver_setup import create_driver
from pages.login import *

def test_login1():
    driver = create_driver()
    driver.get("https://www.flipkart.com/")
    driver.save_screenshot(filename="Evidence.png")
    login_bhumik = LoginPage(driver)
    login_bhumik.login_scenario()

    driver.quit()