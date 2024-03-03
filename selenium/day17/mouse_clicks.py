# //span[text()='right click me']
#
# //span[text()='Copy']
#
# //button[text()='Double-Click Me To See Alert']

from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
# driver.implicitly_wait(20)

act_obj = ActionChains(driver)
###############################right click or context click
# elem1=driver.find_element(By.XPATH, "//span[text()='right click me']")
# act_obj.context_click(elem1).perform()
# elem2=driver.find_element(By.XPATH, "//span[text()='Copy']")
# act_obj.move_to_element(elem2).click().perform()
#
# alt_obj = driver.switch_to.alert
# print(alt_obj.text)
# alt_obj.accept()

###############################
elem1=driver.find_element(By.XPATH, "//button[text()='Double-Click Me To See Alert']")
act_obj.double_click(elem1).perform()

alt_obj = driver.switch_to.alert
print(alt_obj.text)
alt_obj.accept()

sleep(5)
