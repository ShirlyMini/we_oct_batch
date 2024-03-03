from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com")
driver.maximize_window()
driver.implicitly_wait(20)
################################3login

driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")

driver.find_element(By.XPATH, "//button[@type='submit']").click()
sleep(4)
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Customers')]").click()
driver.find_element(By.XPATH, "//ul[@role='menu']/li/ul/li/a/p[contains(text(), 'Customers')]").click()

#####################check boxes###############

#//tbody/tr/td[1]---matches multiple elem
# list_elm = driver.find_elements(By.XPATH, "//tbody/tr/td[1]/input")# ----list of web elem
#
# for elem in list_elm:
#     elem.click()
#     print(elem.is_selected())

####################radio button

driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
# elm = driver.find_element(By.XPATH, "//label[contains(text(),'Male')]/preceding-sibling::input")
elm = driver.find_element(By.XPATH, "//label[contains(text(),'Female')]/preceding-sibling::input")
elm.click()
print(elm.is_selected())
sleep(10)