from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
driver.implicitly_wait(20)

act_obj = ActionChains(driver)
we_tutorials = driver.find_element(By.XPATH, "//span[contains(text(),'Tutorials')]")
we_python_option = driver.find_element(By.XPATH, "/html/body/nav/div/div[1]/ul[1]/li[2]/ul/li[2]/span")
we_python_tuto=driver.find_element(By.XPATH, "/html/body/nav/div/div[1]/ul[1]/li[2]/ul/li[2]/ul/li[1]/a")

act_obj.move_to_element(we_tutorials).move_to_element(we_python_option).move_to_element(we_python_tuto).click().perform()

print(driver.find_element(By.XPATH, "//h1").text)

sleep(10)