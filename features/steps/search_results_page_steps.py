from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")
PROGRESSIVE_SUBNAV = (By.CSS_SELECTOR, '[href*="New-Arrivals"]')
SUBNAV_LOC = (By.CSS_SELECTOR, '.nav-a.nav-hasArrow.nav-active')


@then('Search results for {expected_result} are shown')
def verify_search_results(context, expected_result):
    context.app.search_results_page.verify_search_results(expected_result)


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
    sleep(2)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print(all_products)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Error! Title should not be blank'
        assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Img is not found'


@when('Hover over New Arrivals menu selection')
def hover_subnav(context):
    context.app.search_results_page.hover_subnav(PROGRESSIVE_SUBNAV)


@then('Verify New Arrivals popup is visible')
def verify_subnav_popup(context):
    context.app.search_results_page.verify_subnav_popup(SUBNAV_LOC)
