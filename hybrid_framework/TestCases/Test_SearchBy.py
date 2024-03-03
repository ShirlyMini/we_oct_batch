import sys

import pytest

sys.path.append(r"C:\Users\user\PycharmProjects\pythonProject_WE_October")

from hybrid_framework.Utility.ReadProperty import Read_Property
from hybrid_framework.PageObject import LoginPageObject
from hybrid_framework.PageObject import SearchByPageObj
from hybrid_framework.Utility.CustomLogger import custom_log
from hybrid_framework.TestData.test_data import *

class Test_search_function_002:
    @pytest.mark.sanity
    def test_searchby_email(self, launch_browser):
        logg = custom_log()
        logg.info("TC::test_searchby_email")
        self.driver = launch_browser

        login_obj = LoginPageObject.Login(self.driver)
        self.usrname = Read_Property.GetUsername()
        self.password = Read_Property.GetPassword()
        login_obj.SetEmail(self.usrname)
        logg.info("Successfully given username")
        login_obj.SetPassword(self.password)
        logg.info("Successfully given password")
        login_obj.ClickLogin()
        logg.info("Successfully Logged in")

        search_obj = SearchByPageObj.SearchBy(self.driver)
        search_obj.NavigateCustomerPage()
        search_obj.SetEmailSearch("james_pan@nopCommerce.com")
        search_obj.ClickSearchButton()
        emails = search_obj.GetEmail()

        for e_mail in emails:
            if e_mail == "james_pan@nopCommerce.com":
                logg.info("TC::test_searchby_email=Passed")
                assert True
            else:
                logg.error("TC::test_searchby_email=Failed")
                self.driver.save_screenshot(r'.\ScreenShot\test_searchby_email.png')
                assert False

    @pytest.mark.functionality
    @pytest.mark.parametrize("firstname",search_name['firstname'])
    def test_searchby_firstname(self, launch_browser, firstname):
        logg = custom_log()
        logg.info("TC::test_searchby_firstname")
        self.driver = launch_browser

        login_obj = LoginPageObject.Login(self.driver)
        self.usrname = Read_Property.GetUsername()
        self.password = Read_Property.GetPassword()
        login_obj.SetEmail(self.usrname)
        logg.info("Successfully given username")
        login_obj.SetPassword(self.password)
        logg.info("Successfully given password")
        login_obj.ClickLogin()
        logg.info("Successfully Logged in")

        search_obj = SearchByPageObj.SearchBy(self.driver)
        search_obj.NavigateCustomerPage()
        search_obj.SetFirstName(firstname)
        search_obj.ClickSearchButton()
        names = search_obj.GetNames()

        for name in names:
            if firstname in name:
                logg.info("TC::test_searchby_firstname=Passed")
                assert True
            else:
                logg.error("TC::test_searchby_firstname=Failed")
                self.driver.save_screenshot(r'.\ScreenShot\test_searchby_firstname.png')
                assert False

    @pytest.mark.functionality
    @pytest.mark.parametrize("lastname", search_name['lastname'])
    def test_searchby_lastname(self, launch_browser, lastname):
        logg = custom_log()
        logg.info("TC::test_searchby_lastname")
        self.driver = launch_browser

        login_obj = LoginPageObject.Login(self.driver)
        self.usrname = Read_Property.GetUsername()
        self.password = Read_Property.GetPassword()
        login_obj.SetEmail(self.usrname)
        logg.info("Successfully given username")
        login_obj.SetPassword(self.password)
        logg.info("Successfully given password")
        login_obj.ClickLogin()
        logg.info("Successfully Logged in")

        search_obj = SearchByPageObj.SearchBy(self.driver)
        search_obj.NavigateCustomerPage()
        search_obj.SetLastName(lastname)
        search_obj.ClickSearchButton()
        names = search_obj.GetNames()

        for name in names:
            if lastname in name:
                logg.info("TC::test_searchby_lastname=Passed")
                assert True
            else:
                logg.error("TC::test_searchby_lastname=Failed")
                self.driver.save_screenshot(r'.\ScreenShot\test_searchby_lastname.png')
                assert False

