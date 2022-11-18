from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #EC is a common alias for expected_conditions

# init driver
driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(5) delays every find_element by 5 seconds; checks every 100 ms if element is found
driver.wait = WebDriverWait(driver,10) #10 for fast website, 15 for a slower website

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Car')

# wait for 4 sec
#sleep(4)
btn = (By.NAME, 'btnK1')
driver.wait.until(EC.element_to_be_clickable(btn), message='Search button not clickable')

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'car' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
