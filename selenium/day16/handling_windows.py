from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()
driver.implicitly_wait(20)

# driver.find_element(By.XPATH, "//div[@class='tabpane pullleft']/ul/li[1]/a").click()
# driver.find_element(By.XPATH, "//div[@id='Tabbed']/a/button").click()
# driver.find_element(By.XPATH, "//div[@id='Tabbed']/a/button").click()
# driver.find_element(By.XPATH, "//div[@id='Tabbed']/a/button").click()
# driver.find_element(By.XPATH, "//div[@id='Tabbed']/a/button").click()
# print(driver.window_handles)#[parentid, child1id...]
# print(driver.current_window_handle)
###################single window
# driver.switch_to.window(driver.window_handles[1])
# print(driver.title)
# print(driver.current_window_handle)

###################multiple window
# for handle in driver.window_handles[1:]:
#     driver.switch_to.window(handle)
#     print(driver.title)
#     # driver.close()
#     # driver.quit()
# driver.quit()
# sleep(10)

#################NEW SEPERATE WINdow

driver.find_element(By.XPATH, "//div[@class='tabpane pullleft']/ul/li[2]/a").click()
driver.find_element(By.XPATH, "//div[@id='Seperate']/button").click()
driver.find_element(By.XPATH, "//div[@id='Seperate']/button").click()
driver.find_element(By.XPATH, "//div[@id='Seperate']/button").click()
driver.find_element(By.XPATH, "//div[@id='Seperate']/button").click()

###################single window
# print(driver.current_window_handle)
# driver.switch_to.window(driver.window_handles[1])
# print(driver.title)
# print(driver.current_window_handle)

###################multiple window
for handle in driver.window_handles[1:]:
    driver.switch_to.window(handle)
    print(driver.title)
    driver.save_screenshot(f".\handle_{handle}.png")
    driver.close()
    # driver.quit()
# driver.quit()
sleep(10)