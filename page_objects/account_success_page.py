import time
from selenium.webdriver.common.by import By


class AccountSuccessPage(object):
    def __init__(self, browser):
        self.browser = browser

    def confirm_account_create(self, product):
        self.browser.find_element(By.CSS_SELECTOR, 'div[id="content"] h1')
        self.browser.find_element(By.XPATH, '//a[normalize-space()="Success"]')
        time.sleep(2)

    def submit_continue(self):
        self.browser.find_element(By.XPATH, '//a[@class="btn btn-primary""]').click()
        time.sleep(2)