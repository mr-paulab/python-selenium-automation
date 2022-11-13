from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

#@given('Open Amazon product {product_id} page')
#def open_amazon_product(context, product_id):
#    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@given('Store original window')
def original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original: ', context.original_window)


@when('Click on dog image')
def click_img(context):
    context.driver.find_element(*DOG_IMG).click()


@when('Switch to new window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('Current windows: ', current_windows)
    context.driver.switch_to.window(current_windows[1])


@then('Verify blog is opened')
def verify_blog_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.aboutamazon.com/news/workplace/'))


@then('Close blog')
def close_blog(context):
    context.driver.close()


@then('Return to original window')
def return_to_original(context):
    context.driver.switch_to.window(context.original_window)
