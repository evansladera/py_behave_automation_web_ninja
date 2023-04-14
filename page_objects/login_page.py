import time
from selenium.webdriver.common.by import By


class LoginPage(object):
    def __init__(self, browser):
        self.browser = browser

    def input_username(self, username):
        self.browser.find_element(By.ID, 'input-email').send_keys(username)
        time.sleep(2)

    def input_password(self, password):
        self.browser.find_element(By.ID, 'input-password').send_keys(password)
        time.sleep(2)

    def submit_login(self):
        self.browser.find_element(By.XPATH, '//input[@value="Login"]').click()
        time.sleep(2)