from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
location=r"C:\Users\user\PycharmProjects\pythonProject_WE_October\selenium\day17"

chrome_ops = webdriver.ChromeOptions()
chrome_ops.add_experimental_option("prefs", {"download.default_directory": location})

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_ops)


driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[@type='button']").click()

sleep(10)