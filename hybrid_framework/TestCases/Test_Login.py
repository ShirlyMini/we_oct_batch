import sys

import pytest

sys.path.append(r"C:\Users\user\PycharmProjects\pythonProject_WE_October")

from hybrid_framework.Utility.ReadProperty import Read_Property
from hybrid_framework.PageObject import LoginPageObject
from hybrid_framework.Utility.CustomLogger import custom_log

class Test_login_function_001:
    @pytest.mark.sanity
    def test_verify_title(self, launch_browser):
        logg = custom_log()
        logg.info("TC::test_verify_title")
        self.driver = launch_browser

        logg.info("Successfully Logged in")
        if self.driver.title=="Your store. Login":
            logg.info("TC::test_verify_title=Passed")
            assert True
        else:
            logg.error("TC::test_verify_title=Failed")
            self.driver.save_screenshot(r'.\ScreenShot\test_verify_title.png')
            assert False

    @pytest.mark.sanity
    def test_verify_login(self, launch_browser):
        logg = custom_log()
        logg.info("TC::test_verify_login")
        self.driver = launch_browser
        login_obj=LoginPageObject.Login(self.driver)
        self.usrname = Read_Property.GetUsername()
        self.password = Read_Property.GetPassword()
        login_obj.SetEmail(self.usrname)
        logg.info("Successfully given username")
        login_obj.SetPassword(self.password)
        logg.info("Successfully given password")
        login_obj.ClickLogin()
        logg.info("Login into the application...")
        status = login_obj.VerifyDashbord()
        if status == True:
            login_obj.ClickLogout()
            logg.info("TC::test_verify_login=Passed")
            assert True
        else:
            logg.error("TC::test_verify_login=Failed")
            self.driver.save_screenshot(r'.\ScreenShot\ttest_verify_login.png')
            assert False


