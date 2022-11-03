from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open amazon home page')
def open_amazon_home(context):
    context.driver.get("https://www.amazon.com/")


@when('Click on Cart')
def Click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href*='/gp/cart/view.html?ref_=nav_cart']").click()
