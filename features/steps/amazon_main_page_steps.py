from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem a')
SIGN_IN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-button")
# SEARCH_INPUT = (By.id, 'twotabsearchtextbox')
CART_ICON = (By.CSS_SELECTOR, "#a-row sc-your-amazon-cart-is-empty h2")


@given('Open amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()

@when('Click Returns and Orders')
def click_returns_and_orders(context):
    context.app.main_page.search_order_btn()


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.main_page.click_on_cart()

@then('Verify Your Amazon Cart is empty text')
def verify_cart_empty_txt(context):
    context.app.main_page.cart_empty_txt()


@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search_product(product)


@when('Click on button from SignIn popup')
def click_sign_in(context):
    e = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message='Sign In not clickable')
    e.click()


@then('Verify hamburger menu is present')
def verify_ham_menu_present(context):
    e = context.driver.find_element(*HAM_MENU)
    print(e)
    context.driver.refresh()
    print(e.text)
    print(e)


@then('Verify that footer has {expected_link_count} links')
def verify_link_count(context, expected_link_count):
    expected_link_count = int(expected_link_count)

    links = context.driver.find_elements(*FOOTER_LINKS)

    assert len(links) == expected_link_count, \
        f'Expected {expected_link_count} links, but got {len(links)}'


# @when('Wait for {sec} sec')
# def wait_sec(context, sec):
#     sleep(int(sec))


# @then('Verify Sign In is clickable')
# def verify_sign_in_clickable(context):
#     context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN), message='Sign In not clickable')


# @then('Verify Sign In disappears')
# def verify_sign_in_btn_disappears(context):
#     context.driver.wait.until_not(EC.presence_of_element_located(SIGN_IN), message='Sign In is still visible')
