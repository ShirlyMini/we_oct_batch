from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
driver.implicitly_wait(20)

elm_list = driver.find_elements(By.XPATH,"//a")

for elem in elm_list:
    url = elem.get_attribute("href")
    try:
        # print(url)
        status = requests.get(url)
        if int(status.status_code) < 299:
            print(f"{url}: valid")
        else:
            print(f"{url}: invalid")
    except Exception as e:
        print(f"{url}: invalid {e}")
