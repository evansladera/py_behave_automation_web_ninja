import time
from selenium.webdriver.common.by import By


class SearchPage(object):
    def __init__(self, browser):
        self.browser = browser

    def input_product_name(self, product):
        self.browser.find_element(By.CSS_SELECTOR, '#search > input').send_keys(product)
        time.sleep(2)

    def search_product(self):
        self.browser.find_element(By.CSS_SELECTOR, '//*[@id="search"]/span/button').click()
        time.sleep(2)


