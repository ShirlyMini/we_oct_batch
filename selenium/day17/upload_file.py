from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.foundit.in/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//div[contains(text(),'Upload Resume')]").click()
location=r"C:\Users\user\PycharmProjects\pythonProject_WE_October\selenium\day17\samplefile.pdf"
driver.find_element(By.ID, 'file-upload').send_keys(location)
print(driver.find_element(By.ID, 'pop_upload').is_enabled())

sleep(10)