# install selenium
from time import sleep

from selenium import webdriver


###########################3Chrome
from selenium.webdriver.chrome.service import Service

# webdriver("path to the web driver")
service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)# fetching from website


###########################edge
# from selenium.webdriver.edge.service import Service
#
# service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
# driver = webdriver.Edge(service=service_obj)



###########################Firefox

# from selenium.webdriver.firefox.service import Service
#
# service_obj = Service(r"E:\selenium\drivers\geckodriver.exe")
# driver = webdriver.Firefox()
#
#
driver.maximize_window()
driver.get("https://www.google.com/")
print(driver.title)
sleep(10)
driver.quit()# it will terminate the process of driver

