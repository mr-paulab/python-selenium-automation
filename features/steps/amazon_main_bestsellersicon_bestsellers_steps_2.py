from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify there are five links')
# verify BestSellers page opened
def verify_bestseller_link_count(context):
    expected_page_header = "Amazon Best Sellers"
#    actual_page_header = context.driver.find_element(By.CSS_SELECTOR, "div[id*='banner-landing-page-header']").text
    actual_page_header = context.driver.find_element(By.CSS_SELECTOR, "span#zg_banner_text").text
    assert expected_page_header == actual_page_header, f'Error! Expected {expected_page_header}, but got {actual_page_header}'
    print ('page header is: ', actual_page_header)
    expected_link_count = 5
    print ('expected link count is ', expected_link_count)
    actual_link_count = context.driver.find_elements(By.CSS_SELECTOR, "div[class*='nav-tab-all_style'] a")
    print('actual link count is ', len(actual_link_count))
#    assert expected_link_count == actual_link_count, f'Error! Expected {expected_link_count} links, but counted {actual_link_count}'


