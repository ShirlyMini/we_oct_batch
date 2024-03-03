from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# driver.maximize_window()
#
# act_obj = ActionChains(driver)
#
# s1=driver.find_element(By.ID,"box1")
# s2=driver.find_element(By.ID,"box2")
# s3=driver.find_element(By.ID,"box3")
#
# d1=driver.find_element(By.ID,"box106")
# d2=driver.find_element(By.ID,"box107")
# d3=driver.find_element(By.ID,"box101")
#
# act_obj.drag_and_drop(s1,d1).perform()
# act_obj.drag_and_drop(s2,d2).perform()
# act_obj.drag_and_drop(s3,d3).perform()

###################offset
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()

act_obj = ActionChains(driver)
l_elem=driver.find_element(By.XPATH,"//div[@id='slider-range']/span[1]")
r_elem=driver.find_element(By.XPATH,"//div[@id='slider-range']/span[2]")

print(l_elem.location)#{'x': 59, 'y': 250}
print(r_elem.location)#{'x': 545, 'y': 250}

act_obj.drag_and_drop_by_offset(l_elem,100, 0).perform()
print(l_elem.location)#{'x': 161, 'y': 250}
act_obj.drag_and_drop_by_offset(r_elem,-100, 0).perform()
print(r_elem.location)#{'x': 161, 'y': 250}

sleep(7)
