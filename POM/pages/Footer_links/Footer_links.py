from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

#chrome_options=webdriver.ChromeOptions()
#chrome_options.add_argument('window-size=1400,800')
#chrome_options.add_argument('--headless')

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()


driver.get("http://apexdcsqa.azurewebsites.net")
#driver.execute_script("window.open('https://www.google.it/');")  opening url in new tab
driver.find_element(By.XPATH,"//a[contains(text(),'Home')]").click()


time.sleep(1)
driver.get("http://apexdcsqa.azurewebsites.net")
driver.find_element(By.XPATH,"//a[contains(text(),'Company')]").click()

time.sleep(1)
driver.get("http://apexdcsqa.azurewebsites.net")
driver.find_element(By.XPATH,"//a[contains(text(),'Portfolio')]").click()

time.sleep(1)
driver.get("http://apexdcsqa.azurewebsites.net")
driver.find_element(By.XPATH,"//a[contains(text(),'Blog')]").click()


main=driver.get("http://apexdcsqa.azurewebsites.net")

email_ele=driver.find_element_by_name("email")
print(email_ele.is_enabled())
pass_ele=driver.find_element_by_name("password")
print(pass_ele.is_enabled())

time.sleep(2)
email_ele.send_keys("asharma@datacolor.com")
pass_ele.send_keys("Aa7654321")
driver.find_element_by_name("submit").click()

time.sleep(10)
driver.find_element(By.XPATH,"//a[contains(text(),'Home')]").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Company')]").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Portfolio')]").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.close()

driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,"//a[contains(text(),'Blog')]").click()
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.close()


driver.switch_to.window(driver.window_handles[0])
driver.close()
