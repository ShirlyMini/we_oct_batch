from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

class Login:
    id_email = 'Email'
    id_password = 'Password'
    xpath_submit = "//button[@type='submit']"
    xpath_dashbord = "//h1[contains(text(),'Dashboard')]"
    xpath_logout = "//a[contains(text(),'Logout')]"

    def __init__(self, driver):
        self.driver=driver

    def SetEmail(self, email):
        self.driver.find_element(By.ID, self.id_email).clear()
        self.driver.find_element(By.ID, self.id_email).send_keys(email)

    def SetPassword(self, pswd):
        self.driver.find_element(By.ID, self.id_password).clear()
        self.driver.find_element(By.ID, self.id_password).send_keys(pswd)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.xpath_submit).click()

    def VerifyDashbord(self):
        try:
            return self.driver.find_element(By.XPATH, self.xpath_dashbord).is_displayed()
        except:
            return False

    def ClickLogout(self):
        sleep(2)
        self.driver.find_element(By.XPATH, self.xpath_logout).click()


