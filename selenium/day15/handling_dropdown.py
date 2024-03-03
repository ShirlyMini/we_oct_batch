from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com/signup")
driver.maximize_window()
driver.implicitly_wait(20)

we_day = driver.find_element(By.ID, "day")
we_month = driver.find_element(By.ID, "month")
we_year = driver.find_element(By.ID, "year")

drpdown_day = Select(we_day)
drpdown_day.select_by_index(27)# index is starting from 0 to n-1

drpdown_month = Select(we_month)
drpdown_month.select_by_visible_text("May")

drpdown_year = Select(we_year)
drpdown_year.select_by_value("1990")

sleep(10)