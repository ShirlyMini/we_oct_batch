import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from xluitilities import *
from logutility import logger

service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://cleartax.in/s/simple-compound-interest-calculator")
driver.maximize_window()
# drp_down = Select(driver.find_element(By.ID, "a"))
# drp_down.select_by_value("Simple Interest")

path = r"C:\Users\user\PycharmProjects\pythonProject_WE_October\test_framework\test_data_with_xl\simple_interest.xlsx"
sheet = "Sheet1"
rows = no_rows(path, sheet)
cols = no_col(path, sheet)

for r in range(2, rows+1):# 0 to n-1
    log_var = logger()

    inttype_elem = driver.find_element(By.ID, "a")
    princi_elem = driver.find_element(By.ID, "c")
    rate_elem = driver.find_element(By.ID, "d")
    punit_elem = driver.find_element(By.ID, "f")
    poption_elem = driver.find_element(By.ID, "e")
    total_value_elem = driver.find_element(By.XPATH, "//label[contains(text(),'Total Value')]/following-sibling::span")

    log_var.info("selecting intrest type")
    int_type_drp_down = Select(inttype_elem)
    int_type_drp_down.select_by_visible_text(read_cell(path, sheet, r, 5))

    log_var.info("setting pricipal amt")
    princi_elem.clear()
    princi_elem.send_keys(read_cell(path, sheet, r, 1))
    log_var.info("setting rate")
    rate_elem.clear()
    rate_elem.send_keys(read_cell(path, sheet, r, 2))

    peroid_unit_drp_down = Select(punit_elem)
    peroid_unit_drp_down.select_by_visible_text(read_cell(path, sheet, r, 4))

    poption_elem.clear()
    poption_elem.send_keys(read_cell(path, sheet, r, 3))

    amt = total_value_elem.text
    amt_frm_xl = read_cell(path, sheet, r, 6)
    amt_modified = amt.replace("₹ ", "").replace(",", "")
    print(type(amt_modified), type(amt_frm_xl))
    print(amt_modified, amt_frm_xl)
    write_cell(path, sheet, r, 8, amt)

    if str(amt_modified) == str(amt_frm_xl):
        if read_cell(path, sheet, r, 7) == "Pass":
            write_cell(path, sheet, r, 9, "True")
            green_pattern(path, sheet, r, 9)
            log_var.info("Test passed")
            assert True
        else:
            write_cell(path, sheet, r, 9, "False")
            red_pattern(path, sheet, r, 9)
            log_var.error("Test Failed")
            assert False
    elif str(amt_modified) != str(amt_frm_xl):
        if read_cell(path, sheet, r, 7) == "Fail":
            write_cell(path, sheet, r, 9, "True")
            green_pattern(path, sheet, r, 9)
            log_var.info("Test passed")
            assert True
        else:
            write_cell(path, sheet, r, 9, "False")
            red_pattern(path, sheet, r, 9)
            log_var.error("Test Failed")
            assert False








sleep(5)