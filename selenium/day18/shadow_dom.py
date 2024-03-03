from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://books-pwakit.appspot.com/explore?q=book")
driver.maximize_window()

# driver.find_element(By.ID, 'input').send_keys("book12345")

shadow1 = driver.find_element(By.CSS_SELECTOR, "book-app").shadow_root
shadow1.find_element(By.CSS_SELECTOR, 'input#input').clear()
shadow1.find_element(By.CSS_SELECTOR, 'input#input').send_keys("book12345")

sleep(10)