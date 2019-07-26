from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from pages.homepage.login_page import LoginPage
from pages.Footer_links.Footer_links import validateFooter
from utilities.teststatus import statusCheck
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True) # execute before the test test method
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.sc = statusCheck(self.driver)
        self.vf = validateFooter(self.driver)

    @pytest.mark.run(order=1) # to order the test cases if you have multiple test cases on the same page.
    def testFooter(self):
        self.vf.clickCompanyfooter()
        self.vf.clickBlogfooter()
        self.vf.clickHomefooter()
        self.vf.clickSupportfooter()
        self.vf.clickSupportfooter()

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        # login verification
        loginResult1 = self.lp.verifyLogin()
        self.sc.mark(loginResult1, "Login was successful")
        loginResult2 = self.lp.verifyTitle()
        self.sc.markFinal("test_validLogin", loginResult2, "Title")



