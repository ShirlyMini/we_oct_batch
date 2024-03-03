from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://jqueryui.com/autocomplete/")
# driver.maximize_window()
#
#
# frame_elem = driver.find_element(By.XPATH, '//iframe[@class="demo-frame"]')
# driver.switch_to.frame(frame_elem)
# driver.find_element(By.ID,'tags').send_keys("a")
# sleep(2)
# while True:
#     driver.find_element(By.ID,'tags').send_keys(Keys.ARROW_DOWN)
#     if driver.find_element(By.ID,'tags').get_attribute("value") == "Java":
#         driver.find_element(By.ID, 'tags').send_keys(Keys.ENTER)
#         break
# print(driver.find_element(By.ID,'tags').get_attribute("value"))
# sleep(10)

driver.get("https://money.rediff.com/feedback")
driver.maximize_window()

act_obj = ActionChains(driver)
user_we = driver.find_element(By.NAME,'username')
# phone_we=driver.find_element(By.NAME,'phone')
# email_we=driver.find_element(By.NAME,'emailId')
# comments_we=driver.find_element(By.NAME,'comments')

user_we.send_keys("abc@gmail.com")

#ctrl+a and ctrl+c

act_obj.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
act_obj.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# tab
act_obj.send_keys(Keys.TAB).perform()
#ctrl+v
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

# tab
act_obj.send_keys(Keys.TAB).perform()
#ctrl+v
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

# tab
act_obj.send_keys(Keys.TAB).perform()
#ctrl+v
act_obj.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

sleep(10)