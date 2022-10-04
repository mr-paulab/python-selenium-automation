# Paul Brandon Oct 3, 2022
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

c = webdriver.ChromeOptions()
c.add_argument("--incognito")

# init driver
driver = webdriver.Chrome(options=c)
driver.implicitly_wait(0.5)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').clear().send_keys('milk oolong tea')
driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"milk oolong tea"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'

print('Test case passed')
driver.implicitly_wait(0.5)
driver.quit()




