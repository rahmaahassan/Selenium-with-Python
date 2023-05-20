from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome('/Users/rahmahassan/Downloads/chromedriver_mac64/chromedriver')
driver.get('https://artoftesting.com/sampleSiteForSelenium')

elem1 = driver.find_element(By.ID,'male').click
elem2 = driver.find_element(By.ID,'female').click
elem3 = driver.find_element(By.CLASS_NAME,'Automation').click
elem4 = driver.find_element(By.CLASS_NAME,'Performance').click
elem5 = driver.find_element(By.CLASS_NAME,'mobile-menu').click
elem6 = driver.find_element(By.ID,'automation').click

elem1.send_keys('male', Keys.ENTER)

dropdown = Select(driver.find_element(By.ID, 'testingDropdown'))

dropdown.select_by_visible_text('Database Testing')

print(driver.title)
time.sleep(5)

driver.navigate().to("www.google.com")
print(driver.title)

driver.forward()
time.sleep(5)

driver. close()