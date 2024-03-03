from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# driver.implicitly_wait(20)

# driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
#
# alt_obj = driver.switch_to.alert
# print(alt_obj.text)#
# alt_obj.accept()

# driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
# alt_obj = driver.switch_to.alert
# print(alt_obj.text)#
# # alt_obj.accept()
# alt_obj.dismiss()

# driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
# alt_obj = driver.switch_to.alert
#
# print(alt_obj.text)#
# alt_obj.send_keys("welcome")
# alt_obj.accept()
# # alt_obj.dismiss()
#
#
# sleep(10)

####################################################
import autoit
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
driver.implicitly_wait(20)

autoit.win_wait_active("",30)
autoit.send("admin{TAB}")
autoit.send("admin{ENTER}")

sleep(10)
