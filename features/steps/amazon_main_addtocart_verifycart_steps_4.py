from selenium.webdriver.common.by import By
from behave import then


@then('chosen product is in cart')
def verify_found_results_text(context):
    expected_count = 1
    actual_count = context.driver.find_element(By.CSS_SELECTOR, "span.nav-cart-count").text
    assert expected_count == int(actual_count), f'Error! Expected {expected_count}, but got {actual_count}'
    print("product added to cart")