# iframe(New tags) or frames(stop)


from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://ui.vision/demo/webtest/frames/")
driver.maximize_window()
driver.implicitly_wait(20)

##################Frame
# driver.switch_to.frame(driver.find_element(By.XPATH,"//html/frameset/frame[1]"))# name # id# index# webelem
# print(driver.find_element(By.XPATH, "//form[@id='id1']/div").text)
# driver.find_element(By.XPATH, "//form[@id='id1']/div/input").send_keys("welcome frame 1")
#
# driver.switch_to.default_content()# return to browser
#
# driver.switch_to.frame(driver.find_element(By.XPATH,"//html/frameset/frameset/frame[1]"))
# print(driver.find_element(By.XPATH, "//form[@id='id2']/div").text)
# driver.find_element(By.XPATH, "//form[@id='id2']/div/input").send_keys("welcome frame 2")
#
# driver.switch_to.default_content()
#
# driver.switch_to.frame(driver.find_element(By.XPATH,"//html/frameset/frameset/frame[3]"))
# print(driver.find_element(By.XPATH, "//form[@id='id4']/div").text)
# driver.find_element(By.XPATH, "//form[@id='id4']/div/input").send_keys("welcome frame 4")
#
# driver.switch_to.default_content()
###########################inner frame
driver.switch_to.frame(driver.find_element(By.XPATH,"//html/frameset/frameset/frame[2]"))
print(driver.find_element(By.XPATH, "//form[@id='id3']/div").text)
driver.find_element(By.XPATH, "//form[@id='id3']/div/input").send_keys("before iframe frame 3")

driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe"))
print(driver.find_element(By.XPATH, "//div[@role='heading'][1]").text)

driver.switch_to.parent_frame()
print(driver.find_element(By.XPATH, "//form[@id='id3']/div").text)
driver.find_element(By.XPATH, "//form[@id='id3']/div/input").clear()
driver.find_element(By.XPATH, "//form[@id='id3']/div/input").send_keys("after inner frame frame 3")

driver.switch_to.default_content()
sleep(10)