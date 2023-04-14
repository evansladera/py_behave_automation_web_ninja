import time
from selenium.webdriver.common.by import By


class AccountPage(object):
    def __init__(self, browser):
        self.browser = browser

    def account_create(self, product):
        self.browser.find_element(By.XPATH, '//h2[normalize-space()="My Account"]')
        time.sleep(2)
