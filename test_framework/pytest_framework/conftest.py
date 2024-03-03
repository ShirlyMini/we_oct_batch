import pytest


@pytest.fixture()
def setup():
    print("open browser and login")
    yield
    print("logout and close browser")

@pytest.fixture(scope="class")
def setup_class():
    print("open browser and login-CLASS")
    yield
    print("logout and close browser-CLASS")

@pytest.fixture(scope="module")
def setup_Module():
    print("open browser and login-MODULE")
    yield
    print("logout and close browser-MODULE")

@pytest.fixture()
def setup2():
    print("open browser and login")
    yield True,True
    print("logout and close browser")

###############################
def pytest_configure(config):
    #config.addinivalue_line("markers", "marker_name: desc")
    config.addinivalue_line("markers", "sanity: sanity testing")
    config.addinivalue_line("markers", "regression: regression testing")