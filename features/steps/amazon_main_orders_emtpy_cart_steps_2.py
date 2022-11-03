from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Cart page opens cart empty')
def verify_cart_page_opened(context):
    expected_page_header = "Your Amazon Cart is empty"
    actual_page_header = context.driver.find_element(By.CSS_SELECTOR, "a-row.sc-your-amazon-cart-is-empty").text
    assert expected_page_header == actual_page_header, f'Error! Expected {expected_page_header}, but got {actual_page_header}'
