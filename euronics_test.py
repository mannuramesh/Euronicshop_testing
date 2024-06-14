from pages.euronics_page import EuronicsPage
from pages.products_listing_page import ListingPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
import time


class TestShopPage:

    def test_shop(self, driver):

        search_page = EuronicsPage(driver)
        search_page.open("https://euronics.lv")
        search_page.click_if_cookies_button_visible()
        search_page.search_form_fill_and_proceed()

        listing_page = ListingPage(driver)
        listing_page.click_random_product()

        product_page = ProductPage(driver)
        expected_name = product_page.get_expected_product_name()
        expected_price = product_page.get_expected_product_price()
        print(expected_name)
        print(expected_price)
        product_page.add_to_cart()
        product_page.go_to_cart()

        cart_page = CartPage(driver)
        actual_name = cart_page.get_product_name_in_cart()
        actual_price = cart_page.get_product_price_in_cart()
        print(actual_name)
        print(actual_price)
        cart_page.delete_product_from_cart()

        time.sleep(5)
