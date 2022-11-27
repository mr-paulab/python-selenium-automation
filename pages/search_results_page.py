from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    SELECTED_DEPARTMENT = (By.CSS_SELECTOR, '#nav-subnav[data-category="{SUBSTR}"]')
    PROGRESSIVE_SUBNAV = (By.CSS_SELECTOR, '[href*="New-Arrivals"]')
    SUBNAV_LOC = (By.CSS_SELECTOR, '.nav-a.nav-hasArrow.nav-active')

    def get_department_locator(self, department: str):
        # department = books
        # [ By.CSS_SELECTOR , '#nav-subnav[data-category="books"]'
        return [self.SELECTED_DEPARTMENT[0], self.SELECTED_DEPARTMENT[1].replace('{SUBSTR}', department)]

    def verify_search_results(self, expected_result):
        self.verify_element_text(expected_result, *self.SEARCH_RESULTS)

    def verify_department(self, department):
        print('department => ', department)
        department_locator = self.get_department_locator(department)
        print(department_locator)
        self.wait_for_element_appear(*department_locator)

    def hover_subnav(self, PROGRESSIVE_SUBNAV):
        new_arrivals_option = self.find_element(*PROGRESSIVE_SUBNAV)
#        print('new arrivals option => ', new_arrivals_option)
        hover = ActionChains(self.driver).move_to_element(new_arrivals_option)
        hover.perform()

    def verify_subnav_popup(self, SUBNAV_LOC):
        self.wait.until(EC.visibility_of_element_located(SUBNAV_LOC))
