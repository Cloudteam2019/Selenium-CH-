
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.common.by import By
import time

class validateFooter(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#Locators
    _home_footer = "//a[@href='https://www.datacolor.com/']"
    _company_footer = "//a[contains(text(),'Company')]"
    _portfolio_footer = "//a[contains(text(),'Portfolio')]"
    _blog_footer = "//a[contains(text(),'Blog')]"
    _support_footer = "//a[contains(text(),'Support')]"

# Element Interaction
    def clickHomefooter(self):
        self.elementClick(self._home_footer,locatorType="xpath")
        time.sleep(3)

    def clickCompanyfooter(self):
        self.elementClick(self._company_footer,locatorType="xpath")
        time.sleep(3)

    def clickPortfoliofooter(self):
        self.elementClick(self._portfolio_footer,locatorType="xpath")
        time.sleep(3)

    def clickBlogfooter(self):
        self.elementClick(self._blog_footer,locatorType="xpath")
        time.sleep(3)

    def clickSupportfooter(self):
        self.elementClick(self._support_footer,locatorType="xpath")
        time.sleep(3)