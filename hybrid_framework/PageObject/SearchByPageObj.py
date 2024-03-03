from time import sleep

from selenium.webdriver.common.by import By


class SearchBy:
    xpath_customer_menu = "//ul[@role='menu']/li/a/p[contains(text(),'Customers')]"
    xpath_customer_option = "//ul[@role='menu']/li/ul/li/a/p[contains(text(),'Customers')]"
    id_email="SearchEmail"
    id_firstname="SearchFirstName"
    id_lastname="SearchLastName"
    id_search_button = "search-customers"
    xpath_get_email = "//tbody/tr/td[2]"
    xpath_get_name = "//tbody/tr/td[3]"

    def __init__(self, driver):
        self.driver=driver

    def NavigateCustomerPage(self):
        sleep(2)
        self.driver.find_element(By.XPATH, self.xpath_customer_menu).click()
        sleep(2)
        self.driver.find_element(By.XPATH, self.xpath_customer_option).click()

    def SetEmailSearch(self, email):
        self.driver.find_element(By.ID, self.id_email).send_keys(email)

    def SetFirstName(self, name):
        self.driver.find_element(By.ID, self.id_firstname).send_keys(name)

    def SetLastName(self, name):
        self.driver.find_element(By.ID, self.id_lastname).send_keys(name)

    def ClickSearchButton(self):
        self.driver.find_element(By.ID, self.id_search_button).click()
        sleep(3)

    def GetEmail(self):
        list_of_email = []
        email_list_we = self.driver.find_elements(By.ID, self.xpath_get_email)
        for elem in email_list_we:
            list_of_email.append(elem.text)
        return list_of_email

    def GetNames(self):
        list_of_names = []
        name_list_we = self.driver.find_elements(By.ID, self.xpath_get_name)
        for elem in name_list_we:
            list_of_names.append(elem.text)
        return list_of_names

