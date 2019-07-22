import unittest
import HtmlTestRunner
from tests.homepage.login_tests import LoginTests
from tests.customers.create_new_customer_tests import NewCustomerTests

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(NewCustomerTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)

#unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))