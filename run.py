import  selenium
import  time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testData import *

service = Service(executable_path='C:/Users/ADMIN/AppData/Local/Programs/Python/Python314/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(5)

class UI:

    def open_browser():
        driver.get("https://www.flipkart.com/")
        driver.maximize_window()
        time.sleep(5)


    def login():
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
            driver.close()
        except Exception as e:
            print(e)

UI.open_browser()
UI.login()