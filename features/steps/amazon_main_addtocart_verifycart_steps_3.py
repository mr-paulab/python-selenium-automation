from selenium.webdriver.common.by import By
from behave import when

@when('verify page for product')
#verify page
def verify_found_results_text(context):
    expected_product = "oolong tea"
    actual_product = context.driver.find_element(By.CSS_SELECTOR, "span.a-size-large.product-title-word-break").text.lower()
    if expected_product in actual_product:
        print("page verified for product")
    else:
        print("page not verified for product")


# assume that one time purchase is inactive, subscribe and save is active
@when('click one time purchase button')
def click_onetimepurchase(context):
#    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "i.a-icon.a-accordion-radio.a-icon-radio-inactive"))).click()
    context.driver.find_element(By.CSS_SELECTOR, "i.a-icon.a-accordion-radio.a-icon-radio-inactive").click()
    print("one time purchase button clicked")


# click on add to cart button for single product
@when('click add to cart for single product')
def add_product_to_cart(context):
#    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='submit.add-to-cart'][type='submit']"))).click()
    context.driver.find_element(By.CSS_SELECTOR, "input[name='submit.add-to-cart'][type='submit']").click()