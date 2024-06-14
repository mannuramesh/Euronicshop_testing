from pages.base_page import BasePage
from locators.page_locators import PageLocators as Locators


class EuronicsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click_if_cookies_button_visible(self):
        if Locators.COOKIES_ACCEPT_BUTTON:
            self.element_is_visible(Locators.COOKIES_ACCEPT_BUTTON).click()

    def search_form_fill_and_proceed(self):
        self.element_is_visible(Locators.SEARCH_TEXTFORM).send_keys("apple macbook air m1")
        self.element_is_visible(Locators.SEARCH_DO_BUTTON).click()
