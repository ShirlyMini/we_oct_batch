from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# implicit wait
# driver.implicitly_wait(10)

# explicit wait
wait_obj = WebDriverWait(driver, 10)
# WebDriverWait

driver.get("https://admin-demo.nopcommerce.com/login")

driver.find_element(By.CSS_SELECTOR,"#Email").clear()
driver.find_element(By.CSS_SELECTOR,"input#Email").send_keys("admin@yourstore.com")

driver.find_element(By.CSS_SELECTOR,".password").clear()
driver.find_element(By.CSS_SELECTOR,"input.password").send_keys("admin")

driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()


wait_obj.until(expected_conditions.presence_of_element_located((By.XPATH,"//h1[contains(text(),'Dashboard')]")))
print(driver.find_element(By.XPATH,"//h1[contains(text(),'Dashboard')]").is_displayed())
