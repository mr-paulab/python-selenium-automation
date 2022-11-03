from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Cart empty')
def verify_cart_page_open_empty(context):
    expected_page_header = "Your Amazon Cart is empty"
    actual_page_header = context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2").text
    assert expected_page_header == actual_page_header, f'Error! Expected {expected_page_header}, but got {actual_page_header}'

