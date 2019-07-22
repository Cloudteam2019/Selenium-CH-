"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefoxOptions
import os

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('window-size=1400,800')
        chrome_options.add_argument('--headless')

        # option = firefoxOptions()
        # option.add_argument('window-size=1400,800')
        # option.add_argument('--headless')

        baseURL = "http://apexdcsqa.azurewebsites.net/auth/login"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome(executable_path="C:\\Users\\GSingh\\PycharmProjects\\POM\\drivers\\chromedriver.exe",options=chrome_options)
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)
        #print (driver.capabilities)
        return driver