from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# is_displayed and is_selected
# driver.get("https://admin-demo.nopcommerce.com/login")
# driver.maximize_window()
# elem = driver.find_element(By.XPATH, "//input[@id='RememberMe']")
# print(elem.is_displayed())# true
# if elem.is_displayed():
#     if elem.is_selected() == False:
#         elem.click()
#         print("After clicking checkbox....", elem.is_selected())# True

# is_enabled

driver.get("https://www.linkedin.com/learning-login/")


print(driver.find_element(By.ID, "auth-id-button").is_enabled())
driver.find_element(By.ID, "auth-id-input").send_keys("1234")
print(driver.find_element(By.ID, "auth-id-button").is_enabled())