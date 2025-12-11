from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils.testData import test_data
from pages.common_func import privacy_policy, terms_of_use

class LoginPage:

    def __init__(self, driver):
        self.driver = driver


    def login_scenario(self):
        driver=self.driver
        try:
            driver.find_element(By.XPATH, "//span[text()='Login']").click()
            wait = WebDriverWait(driver, 10, poll_frequency=1)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Request OTP']")))
            values = test_data()
            # print(values)
            for row in values:
                input = driver.find_element(By.XPATH,"(//*[@type='text'])[2]")
                input.send_keys(row)
                try:
                    driver.find_element(By.XPATH,"//button[text()='Request OTP']").click()
                    actual_msg = driver.find_element(By.CLASS_NAME,"AiNWLu").text
                    print(actual_msg)
                    expected_msg = "Please enter valid Email ID/Mobile number"
                    assert actual_msg == expected_msg
                except:
                    print("There you go")
                input.clear()
                time.sleep(2)
            privacy_policy(driver)
            terms_of_use(driver)
            # object.terms_of_use()
            # object.privacy_policy()
        except Exception as e:
            print(e)
        driver.close()


