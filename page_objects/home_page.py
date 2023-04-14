import time
from selenium.webdriver.common.by import By


class HomePage(object):

    url_home_page = 'https://tutorialsninja.com/demo/'

    def __init__(self, browser):
        self.browser = browser

    def my_account_drop_menu(self):
        self.browser.find_element(By.XPATH, '//span[normalize-space()="My Account"]').click()
        time.sleep(2)

    def select_login(self):
        self.browser.find_element(By.XPATH, '//a[normalize-space()="Login"]').click()
        time.sleep(2)

    def select_register(self):
        self.browser.find_element(By.XPATH, '//a[normalize-space()="Register"]').click()
        time.sleep(2)