import sys

import pytest

sys.path.append(r"C:\Users\user\PycharmProjects\pythonProject_WE_October")

from hybrid_framework.Utility.ReadProperty import Read_Property
from hybrid_framework.PageObject import LoginPageObject
from hybrid_framework.Utility.CustomLogger import custom_log
from hybrid_framework.Utility.xluitilities import *

class Test_login_function_002:
    xl_path = r".\TestData\LoginData.xlsx"
    sheet = "Sheet1"
    login_data=[]
    for r in range(2,no_rows(xl_path, sheet)+1):
        temp_list=[]
        for c in range(1,no_col(xl_path, sheet)+1):
            temp_list.append(read_cell(xl_path, sheet,r, c))
        login_data.append(tuple(temp_list))
    print(login_data)
#[('admin@yourstore.com', 'admin', 'Pass'), ('admin@yourstore.com', 'adm', 'Fail'), ('adm@yourstore.com', 'admin', 'Fail'), ('adm@yourstore.com'
# , 'adm', 'Fail')]

    @pytest.mark.functionality
    @pytest.mark.parametrize("user, pswd, expected", login_data)
    def test_verify_login_ddt(self, launch_browser, user, pswd, expected):
        logg = custom_log()
        logg.info("TC::test_verify_login")
        self.driver = launch_browser
        login_obj=LoginPageObject.Login(self.driver)
        self.usrname = user
        self.password = pswd
        login_obj.SetEmail(self.usrname)
        logg.info("Successfully given username")
        login_obj.SetPassword(self.password)
        logg.info("Successfully given password")
        login_obj.ClickLogin()
        logg.info("Login into the application...")
        status = login_obj.VerifyDashbord()
        if status == True and expected=="Pass":
            login_obj.ClickLogout()
            logg.info("TC::test_verify_login=Passed")
            assert True
        elif status == False and expected=="Fail":
            logg.info("TC::test_verify_login=Passed")
            assert True
        else:
            logg.error("TC::test_verify_login=Failed")
            self.driver.save_screenshot(r'.\ScreenShot\ttest_verify_login.png')
            assert False


