from selenium.webdriver.common.by import By
from behave import given, when, then


def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
@when('Click on Returns and Orders')
def Click_returns_orders(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[ID='nav-orders']").click()
