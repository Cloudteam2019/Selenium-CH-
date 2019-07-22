from utilities.teststatus import statusCheck
from pages.customers.create_new_customer_page import createNewCustomerPage
import pytest
import unittest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class NewCustomerTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):
        self.newCustomer = createNewCustomerPage(self.driver)
        self.sc = statusCheck(self.driver)

    @data(*getCSVData("C:\\Users\\GSingh\\PycharmProjects\\POM\\testdata.csv"))
    @unpack
    def test_create_Customer(self,companyname,address,city,state,postalcode,phonenumber,users,guid,contactname,contactemail):
        self.newCustomer.clickAdmin()
        self.newCustomer.clickCustomer()
        self.newCustomer.addNewCustomer()
        self.newCustomer.enterCompanyName(companyname)
        self.newCustomer.enterAddress(address)
        self.newCustomer.enterCity(city)
        self.newCustomer.selectCountry()
        self.newCustomer.enterState(state)
        self.newCustomer.enterPostalCode(postalcode)
        self.newCustomer.enterPhoneNumber(phonenumber)
        self.newCustomer.selectStartContractDate()
        self.newCustomer.selectEndContractDate()
        self.newCustomer.selectAccountType()
        self.newCustomer.enterUsers(users)
        self.newCustomer.enterSFGUID(guid)
        self.newCustomer.enterContactName(contactname)
        self.newCustomer.enterContactEmail(contactemail)
        self.newCustomer.clickSaveButton()