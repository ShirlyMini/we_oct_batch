import sys
sys.path.append(r"C:\Users\user\PycharmProjects\pythonProject_WE_October")
import pytest
from selenium import webdriver
from hybrid_framework.Utility.ReadProperty import Read_Property


@pytest.fixture()
def launch_browser(request):
    if request.config.getoption("--browser")=="chrome":
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif request.config.getoption("--browser")=="edge":
        from selenium.webdriver.edge.service import Service
        service_obj = Service(r"E:\selenium\drivers\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif request.config.getoption("--browser")=="ff":
        from selenium.webdriver.firefox.service import Service
        driver = webdriver.Firefox()
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    base_url = Read_Property.GetURL()
    driver.get(base_url)
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

def pytest_configure(config):
    config.addinivalue_line("markers", "sanity: sanity testing")
    config.addinivalue_line("markers", "functionality: functionality testing")

