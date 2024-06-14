import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.start_page import start_page

driver = webdriver.Chrome()
driver.maximize_window()

search_text = "apple macbook air m1"
start_page("https://www.euronics.lv/")
#driver.get("https://www.euronics.lv/")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "cookie-accept-all-button")))
if driver.find_element(By.ID, "cookie-accept-all-button"):
    driver.find_element(By.ID, "cookie-accept-all-button").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//i[@class=' far fa-search']")))
driver.find_element("xpath", "//input[@class='autocomplete__input']").send_keys(search_text)
driver.find_element("xpath", "//i[@class=' far fa-search']").click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='category__header']")))
search_result_text = driver.find_element("xpath", "//h1[@class='category__header']").text

assert search_result_text in search_text

random_product_number = random.randint(1, 6)
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@class='product-card__title']")))
driver.find_element("xpath", "(//span[@class='product-card__title'])[" + str(random_product_number) + "]").click()

char_remove = ["&nbsp;", "€", "(", ")"]

expected_product_name = driver.find_element("xpath", "(//h1[@class='product__title'])[2]").get_attribute("innerHTML").strip()
expected_product_price = driver.find_element("xpath", "//span[@class='price__original']").get_attribute("innerHTML").strip()
for char in char_remove:
    expected_product_name = expected_product_name.replace(char, "")
    expected_product_price = expected_product_price.replace(char, "")
print(expected_product_name)
print(expected_product_price)
driver.find_element("xpath", "//button[@data-add-to-cart-id]").click()

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h5[@class='product-name']")))
actual_in_cart = driver.find_element("xpath", "//h5[@class='product-name']").get_attribute("innerHTML").strip()
for char in char_remove:
    actual_in_cart = actual_in_cart.replace(char, "")
print(actual_in_cart)
assert expected_product_name in actual_in_cart

time.sleep(1)
driver.close()
driver.quit()
