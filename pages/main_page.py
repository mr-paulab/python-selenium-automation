from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDER_BTN = (By.CSS_SELECTOR, "a[id='nav-orders']")
    CART_ICON = (By.CSS_SELECTOR, "a[id='nav-cart']")
    CART_TXT = (By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2")
    ADDTOCART_BTN = (By.ID, 'add-to-cart-button')

    def open_main(self):
        self.open_url()

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)

    def search_order_btn(self):
        self.find_element(*self.ORDER_BTN)
        self.click(*self.ORDER_BTN)


    def click_on_cart(self):
        self.find_element(*self.CART_ICON)
        self.click(*self.CART_ICON)


    def cart_empty_txt(self):
        self.find_element(*self.CART_TXT)


    def add_to_cart_btn(self):
        self.find_element(*self.ADDTOCART_BTN)
        self.click(*self.ADDTOCART_BTN)


