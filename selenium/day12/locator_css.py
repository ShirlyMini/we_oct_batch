from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
#ID
# driver.find_element(By.CSS_SELECTOR,"#Email")
# (or)
driver.find_element(By.CSS_SELECTOR,"#Email").clear()
driver.find_element(By.CSS_SELECTOR,"input#Email").send_keys("admin@yourstore.com")

#TAG/CLASS

driver.find_element(By.CSS_SELECTOR,".password").clear()
driver.find_element(By.CSS_SELECTOR,"input.password").send_keys("admin")

##TAG/ATTRIBUTE
driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()

# TAG/CLASS/ATTRIBUTE
driver.find_element(By.CSS_SELECTOR,"input.form-control[type=text]").send_keys("abcd")

sleep(10)