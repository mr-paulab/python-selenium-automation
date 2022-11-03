from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

#PG_HDR = (By.CSS_SELECTOR, "div.help-content h1")

@given('Open cou page')
def open_cou_pg(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html?nodeId=508088&ref_=footer_cou")


@when('Store original windows')
def original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Original: ', context.original_window)


@when('Click on Amazon Privacy Notice link')
# in the body of text
def click_apn_link(context):
    element = context.driver.find_element(By.CSS_SELECTOR, "[href='https://www.amazon.com/privacy']").click()


#@when('Switch to new window')
#def switch_to_new_window(context):
#    context.driver.wait.until(EC.new_window_is_opened)
#    current_windows = context.driver.window_handles
#    print('Current windows: ', current_windows)
#    context.driver.switch_to.window(current_windows[1])


@then('Verify Amazon Privacy Notice page is opened')
def verify_apn_page_opened(context):
    context.driver.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.help-content h1'), 'Amazon.com Privacy Notice'))
    print('Amazon Privacy Notice page verified')

@then('Close new window and switch back to original')
def close_blog(context):
    context.driver.close()
    print('Amazon Privacy Notice page closed')
    context.driver.switch_to.window(context.original_window)
    print('Returned to COU page')


