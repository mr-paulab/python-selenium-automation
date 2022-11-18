from selenium.webdriver.common.by import By
from behave import given, when

# @given('Open amazon page')
# def open_amazon(context):
#   context.driver.get('https://www.amazon.com/')


@when('Click on Returns and Orders')
def click_returns_orders(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[ID='nav-orders']").click()
