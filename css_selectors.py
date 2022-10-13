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

# By tag & id
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
# By id
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
driver.find_element(By.ID, "twotabsearchtextbox")

# By class
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag-us")
# By multiple classes
driver.find_element(By.CSS_SELECTOR, ".icp-nav-flag.icp-nav-flag-us")
# By tag & class
driver.find_element(By.CSS_SELECTOR, "span.icp-nav-flag-us")

# By attribute
driver.find_element(By.CSS_SELECTOR, "input[type='email']")
driver.find_element(By.CSS_SELECTOR, "input[name='email']")
driver.find_element(By.CSS_SELECTOR, "[name='email']")
driver.find_element(By.CSS_SELECTOR, "[href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&nodeId=508088']")
# By multiple attributes
driver.find_element(By.CSS_SELECTOR, "input[name='email'][type='email']")
driver.find_element(By.CSS_SELECTOR, "input[name='email'][type='email'][maxlength='128']")

# By attribute and class
driver.find_element(By.CSS_SELECTOR, "input.a-button-input[type='submit']")

# By partial attribute
driver.find_element(By.CSS_SELECTOR, "[href*='ap_signin_notification_condition_of_use']")
# By partial class - turn into an attribute
driver.find_element(By.CSS_SELECTOR, "a[class*='a-button']")

# From parent element to child
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*='condition']")
driver.find_element(By.CSS_SELECTOR, "div.a-box-inner.a-padding-extra-large a[href*='condition']")

# Xpath backwards from child to parent
driver.find_element(By.XPATH, "//*[./a[contains(@href, 'signin_notification_conditions_of_use')]]")


