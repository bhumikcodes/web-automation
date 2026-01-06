from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def create_driver():
    service = Service(executable_path='C:/Users/ADMIN/AppData/Local/Programs/Python/Python314/chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver