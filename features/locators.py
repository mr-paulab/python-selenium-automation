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

# by href
#driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")

# by aria-label
# driver.find_element(By.XPATH, "//a[@aria-label='Amazon']")

# by text
# driver.find_element(By.XPATH, "//a[text()='Best Sellers']")

# by multi attribute
# driver.find_element(By.XPATH,