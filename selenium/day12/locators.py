# address for the web elemnt in the page
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.maximize_window()
# to open developer tool press ctrl+shift+i

# <input class="email input-validation-error" value="admin@yourstore.com" autofocus="autofocus"
# type="email" data-val="true" data-val-email="Wrong email" data-val-required="Please enter your email"
# id="Email" name="Email" aria-describedby="Email-error" aria-invalid="true"
# data-gtm-form-interact-field-id="1">

# locators
#########
# normal locator
# --->
# id(fastest name)
# classname
# name
# tagname
# linktext/partial linktext---anchor tag<a>--->innertext<


# custom locator
# ---->
# xpath
# css
####################################33
# ID

print(driver.find_element(By.TAG_NAME, "strong").text)#Welcome, please sign in!

print(driver.find_element(By.ID, "Email"))#<selenium.webdriver.remote.webelement.WebElement (session="0b1ad014e6476d924201cc5d7c37d6a6", element="AF7D237F99794C3CAC3E62654F79BEEE_element_1")>
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")

# click remeber me
driver.find_element(By.NAME, "RememberMe").click()
# click sumbit
driver.find_element(By.CLASS_NAME, "button-1").click()
sleep(5)
if driver.find_element(By.CLASS_NAME,"content-header").is_displayed():
    driver.find_element(By.LINK_TEXT, "Logout").click()
    print(driver.find_element(By.TAG_NAME, "strong").text)  # Welcome, please sign in!

sleep(20)

# chropath
#https://chromewebstore.google.com/detail/ljngjbnaijcbncmcnjfhigebomdlkcjo