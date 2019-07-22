import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class createNewCustomerPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _dc_admin_setup_tab = "//*[contains(text(),'Admin')]"
    _customer_tab = "//*[@id=\"customers\"]/ul/li[1]/a/span[2]"
    _add_customer_button = "/html/body/app-my-app/app-layout/div/div[2]/app-customers-page/div/div/div/div/div[2]/app-all-customers/dx-data-grid/div/div[4]/div/div/div[3]/div[1]/div/div"
    _company_field = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _address_field = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _city_field = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _click_country_field = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _select_country = "//div[contains(text(),'Antigua and Barbuda')]"
    _state_field = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _postal_code_field = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _phone_number_field = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _start_contract_calander = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"
    _start_contract_date = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[4]"
    _end_contract_calander = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"
    _end_contract_year_tab = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[2]/div[1]"
    _end_contract_year = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/a[3]/div[1]"
    _end_contract_month = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[3]"
    _end_contract_day = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[5]"
    _account_type = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]"
    _enterprise_account_type = "//div[contains(text(),'Enterprise')]"
    _user_field = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _sf_guid_field = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _contact_name_field = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[7]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _contact_email_field = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/div[1]/div[1]/div[1]/div[7]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]"
    _save_button = "/html[1]/body[1]/app-my-app[1]/app-layout[1]/div[1]/div[2]/app-customers-page[1]/div[1]/div[1]/div[1]/div[1]/div[2]/app-all-customers[1]/dx-data-grid[1]/div[1]/div[6]/div[2]/table[1]/tbody[1]/tr[1]/td[1]/div[2]/div[1]/div[1]/span[1]"


    # Element Interactions

    def clickAdmin(self):
        self.elementClick(self._dc_admin_setup_tab, locatorType="xpath")

    def clickCustomer(self):
        self.elementClick(self._customer_tab,locatorType="xpath")
        time.sleep(5)
    def addNewCustomer(self):
        self.elementClick(self._add_customer_button,locatorType="xpath")
    def enterCompanyName(self, companyname):
        self.sendKeys(companyname,self._company_field, locatorType="xpath")

    def enterAddress(self, address):
        self.sendKeys(address,self._address_field,locatorType="xpath")

    def enterCity(self, city):
        self.sendKeys(city, self._city_field,locatorType="xpath")

    def selectCountry(self):
        self.elementClick(self._click_country_field, locatorType="xpath")
        time.sleep(2)
        self.elementClick(self._select_country, locatorType="xpath")

    def enterState(self, state):
        self.sendKeys(state, self._state_field,locatorType="xpath")

    def enterPostalCode(self, postalcode):
        self.sendKeys(postalcode, self._postal_code_field,locatorType="xpath")

    def enterPhoneNumber(self, phonenumber):
        self.sendKeys(phonenumber, self._phone_number_field,locatorType="xpath")

    def selectStartContractDate(self):
        self.elementClick(self._start_contract_calander,locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._start_contract_date, locatorType="xpath")

    def selectEndContractDate(self):
        self.elementClick(self._end_contract_calander,locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._end_contract_year_tab,locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._end_contract_year, locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._end_contract_month, locatorType="xpath")
        time.sleep(1)
        self.elementClick(self._end_contract_day, locatorType="xpath")

    def selectAccountType(self):
        self.elementClick(self._account_type, locatorType="xpath")
        self.elementClick(self._enterprise_account_type, locatorType="xpath")

    def enterUsers(self, users):
        self.sendKeys(users, self._user_field, locatorType="xpath")

    def enterSFGUID(self, sfguid):
        self.sendKeys(sfguid, self._sf_guid_field, locatorType="xpath")

    def enterContactName(self, contactname):
        self.sendKeys(contactname, self._contact_name_field, locatorType="xpath")

    def enterContactEmail(self, contactemail):
        self.sendKeys(contactemail, self._contact_email_field, locatorType="xpath")

    def clickSaveButton(self):
        self.elementClick(self._save_button,locatorType="xpath")

