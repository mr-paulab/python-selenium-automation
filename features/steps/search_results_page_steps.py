from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-tyype='s-search-result']//a[.//")
SEARCH_RESULTS = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


@then('Search results for {expected_result} are shown')
def verify_search_results(context, expected_result):
    # actual_result = context.driver.find_element(*SEARCH_RESULTS).text
    # assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'
    context.app.search_results_page.verify_search_results(expected_result)


@when('Clock on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
    sleep(2)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print(all_products)
    
