from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-tyype='s-search-result']//a[.//")
SEARCH_RESULTS = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


@then('Search results for {expected_result} are shown')
def verify_search_results(context, expected_result):
    expected_result = '"' + expected_result + '"'
    context.app.search_results_page.verify_search_results(expected_result)


@then('click to display one product page')
def clicktodisplayoneproduct(context):
    context.app.search_results_page.find_element(By.CSS_SELECTOR, "div.a-section.aok-relative.s-image-square-aspect").click()
    print("one product chosen")


@then('click one-time purchase button')
def clickforonetimepurchase(context):
    context.app.search_results_page.find_element(By.CSS_SELECTOR, "i.a-icon.a-accordion-radio.a-icon-radio-inactive").click()
    print("one-time purchase button clicked")
    sleep(5)

@then('click add to cart button')
def click_addtocart_btn(context):
    context.app.main_page.add_to_cart_btn()
    print("add to cart button clicked")
    sleep(5)


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
    sleep(5)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print(all_products)
    
