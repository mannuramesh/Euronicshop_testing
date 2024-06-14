from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def element_is_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(ec.visibility_of_all_elements_located(locator))
