import  selenium
import  time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='C:/Users/ADMIN/AppData/Local/Programs/Python/Python314/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(5)
driver.close()