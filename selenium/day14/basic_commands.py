from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/feedback")
driver.maximize_window()

# find_elem vs find_elems

# print(driver.find_element(By.XPATH, "//input[@name='username']"))# ---webelement
#with signle matching elem
# driver.find_element(By.XPATH, "//input[@name='username']").send_keys("name1")

#with multiple matching elem
# driver.find_element(By.XPATH, "//input[@type='text']").send_keys("name1")

# with invalid xpath
# driver.find_element(By.XPATH, "//input[@type='textdsfef']").send_keys("name1")
#selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element



############find_elemnts
# print(driver.find_elements(By.XPATH,"//input[@type='text']"))# list of webelemts
# sleep(3)
#with multiple matching elem
# elem_list = driver.find_elements(By.XPATH,"//input[@type='text']")
# for elem in elem_list:
#     elem.send_keys("name123")

# with signle matching elem
# elem_list = driver.find_elements(By.XPATH,"//input[@name='username']")# list conatins sigle elem
# for elem in elem_list:
#     elem.send_keys("name123")

# with invalid xpath
# print(driver.find_elements(By.XPATH,"//input[@name='usernamedscdea']"))# []
# sleep(3)