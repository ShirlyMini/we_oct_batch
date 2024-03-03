from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://money.rediff.com/feedback")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("name1")
print(driver.find_element(By.XPATH, "//input[@name='username']").text)# innertext
print(driver.find_element(By.XPATH, "//input[@name='username']").get_attribute("value"))
print(driver.find_element(By.XPATH, "//b").text)