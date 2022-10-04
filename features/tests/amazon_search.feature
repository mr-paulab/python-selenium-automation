from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')