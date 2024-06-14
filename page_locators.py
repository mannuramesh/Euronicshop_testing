from selenium.webdriver.common.by import By
from random import randint


class PageLocators:
    COOKIES_ACCEPT_BUTTON = (By.ID, "cookie-accept-all-button")
    SEARCH_TEXTFORM = (By.XPATH, "//input[@class='autocomplete__input']")
    SEARCH_DO_BUTTON = (By.XPATH, "//i[@class=' far fa-search']")
    SEARCH_RESULT_HEADER = (By.XPATH, "//h1[@class='category__header']")
    RANDOM_PRODUCT_LINK = (By.XPATH, f"(//span[@class='product-card__title'])[{randint(1, 6)}]")
    EXPECTED_PRODUCT_NAME_PRODUCT_PAGE = (By.ID, "product-description")
    EXPECTED_PRODUCT_PRICE_PRODUCT_PAGE = (By.XPATH, "(//span[@class='price__original'])[2]")
    ADD_TO_CART = (By.XPATH, "//button[@data-add-to-cart-id]")
    GO_TO_CART_BUTTON = (By.XPATH, "//a[@class='button w-100']")
    ACTUAL_PRODUCT_NAME_CART = "//a[@class='cart-item__title']"
    ACTUAL_PRODUCT_PRICE_CART = "//p[@class='price__em ']"
    DELETE_PRODUCT_FROM_CART = (By.XPATH, "//button[@class='button button--ghost remove-item']")
    CHECK_IF_PRODUCT_DELETED = (By.XPATH, "//span[@class='noproducts']")
