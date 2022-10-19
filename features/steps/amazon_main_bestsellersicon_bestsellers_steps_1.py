from selenium.webdriver.common.by import By
from behave import given, when, then


#@given('Open amazon home page')
#def open_amazon_home(context):
#    context.driver.get("https://www.amazon.com/")


@when('Click on BestSellers')
def Click_bestsellers_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href*='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()
