from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.base_page import Page


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.ID, 'nav-orders')
    LANG_SELECTION = (By.CSS_SELECTOR, ".icp-nav-flag-us")
    SPANISH_LANG = (By.CSS_SELECTOR, '#nav-flyout-icp [href="#switch-lang=es_US"]')
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')
    PROGRESSIVE_SUBNAV = (By.CSS_SELECTOR, '[href*="New-Arrivals"]')
    SUBNAV_LOC = (By.CSS_SELECTOR, '.nav-a.nav-hasArrow.nav-active')

    def open_main(self):
        self.open_url()

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def click_returns_and_orders_btn(self):
        self.click(*self.ORDERS_BTN)

    def verify_lang(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

    def select_department(self, selection_value):
        select = Select(self.find_element(*self.DEPARTMENT_SELECTION))
        select.select_by_value(f'search-alias={selection_value}')
