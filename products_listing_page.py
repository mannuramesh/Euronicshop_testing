from pages.base_page import BasePage
from locators.page_locators import PageLocators as Locators


class ListingPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def click_random_product(self):
        self.element_is_visible(Locators.RANDOM_PRODUCT_LINK).click()
