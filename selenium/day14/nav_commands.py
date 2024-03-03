from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.linkedin.com/learning-login/")
sleep(2)
driver.refresh()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.refresh()
driver.back()
print("after driver.back",driver.title)
driver.forward()
print("after driver.forward",driver.title)