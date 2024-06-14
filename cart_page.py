import time

from pages.base_page import BasePage
from locators.page_locators import PageLocators as Locators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_product_name_in_cart(self):
        time.sleep(5)
        # self.element_is_visible(Locators.ACTUAL_PRODUCT_NAME_CART)
        actual_name_cart = self.driver.find_element("xpath", Locators.ACTUAL_PRODUCT_NAME_CART).text.encode("UTF-8")
        return actual_name_cart

    def get_product_price_in_cart(self):
        time.sleep(5)
        # self.element_is_visible(Locators.ACTUAL_PRODUCT_PRICE_CART)
        actual_price_cart = self.driver.find_element("xpath", Locators.ACTUAL_PRODUCT_PRICE_CART).text.encode("UTF-8")
        return actual_price_cart

    def delete_product_from_cart(self):
        self.element_is_visible(Locators.DELETE_PRODUCT_FROM_CART).click()
