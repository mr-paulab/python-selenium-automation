from selenium.webdriver.common.by import By
from behave import when, given, then
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product product_id page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


#@when('product page displays')
#@when('product page product_id displays')
#def verify_product_page(context):
#    context.driver.wait.until(EC.url_contains({product_id}), message='web page did not load in time')
#def verify_product_page(context):
#    context.driver.wait.until(EC.url_contains('{product_id}'), message='web page did not load in time')
#def verify_product_page(context):
#    context.driver.wait.until(EC.url_contains(product_id), message='web page did not load in time')
#    print("page for product loaded")
#def verify_product_page(context, product_id):
#    context.driver.wait.until(EC.url_contains({product_id}), message='web page did not load in time')
#def verify_product_page(context, product_id):
#    context.driver.wait.until(EC.url_contains('{product_id}'), message='web page did not load in time')
#def verify_product_page(context, product_id):
#    context.driver.wait.until(EC.url_contains(product_id), message='web page did not load in time')
#    print("page for product loaded")


@then('Verify can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Black/Flannel', 'Grey Marl/Black', 'Loden Marl/Khaki', 'Navy Marl/Navy/Navy Marl']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:4]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print(current_color)
        actual_colors += [current_color]

    assert expected_colors == actual_colors, \
        f'Expected colors {expected_colors} did not match actual {actual_colors}'
