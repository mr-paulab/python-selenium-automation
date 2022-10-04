# HW2 -- Oct 3, 2022
####
#
#  Part 1
#
# Repeat everything I coded during the class.  Done  PAB
# Register for Codewars.  Done
# Review class presentation. Done
# Read about XPATH: https: // www.guru99.com / xpath - selenium.html.  Done
###
#
#  Part 2 - Sign In locators
#
# Amazon logo using attribute @class
# //*[@class='a-icon a-icon-logo']
#
# email input box present
#//*[@id="ap_email"]
#
# Continue button
# //*[@id='continue' and @type='submit']
#
# span alone
#//span[@class='a-expander-prompt']
# contains alone
#//*[contains(text(),'Need help?')]
# span and contains combined
#//span[@class='a-expander-prompt' and contains(text(),'Need help?')]
#
# Forgot your password xpath
#//*[@id="auth-fpp-link-bottom" and contains(text(),'Forgot your password?')]
#
# by ID
#//*[@id="ap-other-signin-issues-link"]
# Other Issues xpath
#//*[@id="ap-other-signin-issues-link" and contains(text(),'Other issues')]
#
# Create account button
#//*[@id="createAccountSubmit"]
# Create account button and contains
#//*[@id="createAccountSubmit" and contains(text(),'Create your Amazon account')]
#
# Conditions of Use
#//*[@id="a-page"]/div[1]/div[4]/div[2]/a[1]
#
# Privacy Notice
#//*[@id="a-page"]/div[1]/div[4]/div[2]/a[2]
#
#
# Paul Brandon Oct 3, 2022
from time import sleep

import h1 as h1
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

driver.implicitly_wait(0.5)

driver.find_element(By.ID, "nav-orders").click()
driver.find_element(By.XPATH, "//*[@class='a-box-inner a-padding-extra-large']/h1")
expected_result_signin_page = 'Sign in'
actual_result_signin_page = driver.find_element(By.XPATH, "//*[@class='a-box-inner a-padding-extra-large']/h1").text
assert expected_result_signin_page == actual_result_signin_page, f'Error! Expected {expected_result_signin_page}, but got {actual_result_signin_page}'

print('Signin Page Test case passed')

driver.implicitly_wait(1.5)

actual_result_email_present = driver.find_element(By.ID, "ap_email")
assert actual_result_email_present, f'Error! Did not find email input'

print('Email input Test case passed')

driver.implicitly_wait(1.5)
driver.quit()






