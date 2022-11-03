from selenium.webdriver.common.by import By
from behave import then


@then('Verify Sign In page opened')
def verify_sign_in_page_opened(context):
    expected_page_header = "Sign in"
    actual_page_header = context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small").text
    assert expected_page_header == actual_page_header, f'Error! Expected {expected_page_header}, but got {actual_page_header}'
    assert context.driver.find_element(By.CSS_SELECTOR, "input#ap_email").is_displayed(), "email field not shown"
