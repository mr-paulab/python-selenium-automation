from selenium.webdriver.common.by import By
from behave import then
from selenium.webdriver.support import expected_conditions as EC #EC is a common alias for expected_conditions

@Then('Verify Sign In URL opened')
def verify_sign_in_url_opened(context):
    context.driver.wait.until(EC.url_contains('ap/signin'), message='Sign In URL did not open')