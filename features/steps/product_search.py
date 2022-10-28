from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')
#The webdriver will wait for a page to load by default via .get() method.
    print("google page opened")


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    print("search term typed")
#    sleep(4)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
    print("search icon is clickable")
    context.driver.find_element(*SEARCH_SUBMIT).click()
    print("search icon clicked")
#    sleep(1)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.driver.wait.until(EC.url_contains(search_word), message='URL does not contain search word in time')
    print("URL contains search_word")
#assertion also tests that the search_word is in the URL
    assert search_word.lower() in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
    print("assert confirms search term in URL")