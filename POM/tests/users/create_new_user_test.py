from utilities.teststatus import statusCheck
from pages.users.create_new_user_page import createNewUserPage
import pytest
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class NewUserTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):
        self.newUser = createNewUserPage(self.driver)
        self.sc = statusCheck(self.driver)

    def test_new_user(self):
        self.newUser.createNewUser()

    def test_user_check(self):
        userResult = self.newUser.validateUser()
        self.sc.markFinal("test_user_check", userResult, "User Check")