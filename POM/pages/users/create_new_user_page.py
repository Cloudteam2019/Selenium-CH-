import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class createNewUserPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _dc_admin_setup_tab = "//*[contains(text(),'Admin')]"
    _user_tab = "//span[contains(text(),'Users')]"
    _add_tab = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-users-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-users[1]/div[1]/dx-data-grid[1]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]"
    _email_box = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-users-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-users[1]/div[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _name_box = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-users-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-users[1]/div[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _password_box = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-users-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-users[1]/div[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _password_confirmation_box = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-users-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-users[1]/div[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _customer_dropdown = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-users-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-users[1]/div[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _test_mill1_selection = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[5]/div[1]"
    _save_user_button = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-users-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-users[1]/div[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/div[1]"
    _search_user_box = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-users-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-users[1]/div[1]/dx-data-grid[1]/div[1]/div[5]/div[2]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/div[2]/div[1]/div[1]/input[1]"
    _search_user = "//td[contains(text(),'test27@email.com')]"

    # element Interactions
    def clickAdminTab(self):
        self.elementClick(self._dc_admin_setup_tab, locatorType= "xpath")

    def clickUserTab(self):
        self.elementClick(self._user_tab, locatorType="xpath")

    def clickAddTab(self):
        self.elementClick(self._add_tab, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_box, locatorType="xpath")

    def enterName(self, name):
        self.sendKeys(name, self._name_box, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_box, locatorType="xpath")

    def confirmPassword(self, confirmpassword):
        self.sendKeys(confirmpassword, self._password_confirmation_box, locatorType="xpath")

    def chooseCustomer(self):
        self.elementClick(self._customer_dropdown, locatorType="xpath")
        time.sleep(2)
        self.elementClick(self._test_mill1_selection, locatorType="xpath")
        self.elementClick(self._save_user_button, locatorType="xpath")

    def searchUser(self, useremail):
        self.sendKeys(useremail,self._search_user_box, locatorType="xpath")

    def confirmUser(self):
        self.isElementPresent(self._search_user, locatorType="xpath")

    # create user
    def createNewUser(self):
        self.clickAdminTab()
        self.clickUserTab()
        time.sleep(3)
        self.clickAddTab()
        self.enterEmail("test27@email.com")
        self.enterName("seleniumtester4")
        self.enterPassword("Tester123")
        self.confirmPassword("Tester123")
        self.chooseCustomer()

    # validate user
    def validateUser(self):
        self.searchUser("test27@email.com")
        time.sleep(3)
        self.confirmUser()