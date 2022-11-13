from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
# EC is a common alias for expected_conditions
from time import sleep

HAM_MENU = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem a')
SIGN_IN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-button")
# SEARCH_INPUT = (bY.id, 'twotabsearchtextbox')


@given('Open amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    # element = context.driver.find_element(By.ID, 'twotabsearchtextbox')
    # element.clear()
    # element.send_keys(product)
    # context.driver.find_element(By.ID, 'nav-search-submit-button').click()
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
