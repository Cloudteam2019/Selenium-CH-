import pytest
from selenium import webdriver
import os
from base.webdriverfactory import WebDriverFactory
from pages.homepage.login_page import LoginPage

#fixuters provide a fixed baseline upon which tests can reliably and repeatedly execute
# pytest.fixture() - Executes specific method before every test method
# pytest.yield() - Executes specific method before and after every test method

@pytest.yield_fixture() # execute specifix method before & after every test method
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print ("Running the test in ---------------------", browser)
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("gsingh@datacolor.com", "Datacolor10")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")