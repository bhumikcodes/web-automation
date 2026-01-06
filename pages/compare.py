from pages.common_func import *

class ComparePage:

    def compare(driver):
        return
    
    def OpenLinks(driver):
        try:
            links  = driver.find_elements(By.XPATH,"//a[@rel='noopener noreferrer']/descendant::div[@class='RG5Slk']")
            count = len(links)
            print("Count of mobiles :" + str(count))
            for i in range(count):
                links[i].click()
                mob_name = links[i].text
                time.sleep(3)
                driver.switch_to.window(driver.window_handles[1])
                wait(driver,element="//button[text()='Buy Now']")
                print(mob_name + "Opened")
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                print("Tab closed")
                time.sleep(2)
        except Exception as e:
            print(e)
        return
