from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time
from base.basepage import BasePage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _email_field = "//input[@name='email']"
    _password_field = "//input[@name='password']"
    _login_button = "//button[@name='submit']"

    # methods
    def enterEmail(self, email):
        self.sendKeys(email,self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType= "xpath")

    # Login
    def login(self, email ="", password =""):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    # verify login is successful
    def verifyLogin(self):
        loginResult = self.isElementPresent("Test Brand", locatorType="plink")
        return loginResult

    # verify Title
    def verifyTitle(self):
        return self.verifyPageTitle("Color")




