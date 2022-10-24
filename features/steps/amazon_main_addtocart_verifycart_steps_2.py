from selenium.webdriver.common.by import By
from behave import when


# Search results page displayed
@when('oolong tea search results displayed')
def verify_search_results(context):
    expected_result = '"' + 'oolong tea' + '"'
    print(expected_result)
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'


# click on one product entry to display product page
@when('click to display one product page')
def clicktodisplayoneproduct(context):
    context.driver.find_element(By.CSS_SELECTOR, "div.a-section.aok-relative.s-image-square-aspect").click()
