# xpath- dom stuc--tree
# xpath-
# absolute xpath = /node1/node2/node3...
# relative= //node11[]


#/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()

# absolute xpath
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input").clear()
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input").send_keys("admin@yourstore.com")
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input").clear()
driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input").send_keys("admin")

# relative xpath

driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//button[@class='button-1 login-button']").click()

print(driver.title)

#https://money.rediff.com/feedback
#//input[@type='text' and @name="emailId"]




