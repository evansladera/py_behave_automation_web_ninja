import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class RegisterPage(object):

    def __init__(self, browser):
        self.browser = browser

    def input_firstname(self, firstname):
        self.browser.find_element(By.ID, 'input-firstname').send_keys(firstname)

    def input_lastname(self, lastname):
        self.browser.find_element(By.ID, 'input-lastname').send_keys(lastname)

    def input_email(self, email):
        self.browser.find_element(By.ID, 'input-email').send_keys(email)

    def input_telephone(self, telephone):
        self.browser.find_element(By.ID, 'input-telephone').send_keys(telephone)

    def input_password(self, password):
        self.browser.find_element(By.ID, 'input-password').send_keys(password)

    def input_confirm_password(self, confirm_password):
        self.browser.find_element(By.ID, 'input-confirm').send_keys(confirm_password)

    def select_yes_newsletter(self):
        self.browser.find_element(By.XPATH, '//label[normalize-space()="Yes"]//input[@name="newsletter"]').click()
        time.sleep(2)

    def select_no_newsletter(self):
        self.browser.find_element(By.XPATH, '//input[@value="0"]').click()
        time.sleep(2)

    def select_agree_privacy_policy(self):
        self.browser.find_element(By.XPATH, '//input[@name="agree"]').click()
        time.sleep(2)

    def submit_register(self):
        self.browser.find_element(By.CSS_SELECTOR, 'div#content input.btn.btn-primary').click()
        time.sleep(2)


class RegisterPageAlerts(object):
    def __init__(self, browser):
        self.browser = browser

    def msgs_alerts(self):
        msg_alert_firstname = 'First Name must be between 1 and 32 characters!'
        msg_alert_lastname = 'Last Name must be between 1 and 32 characters!'
        msg_alert_email = 'E-Mail Address does not appear to be valid!'
        msg_alert_telephone = 'Telephone must be between 3 and 32 characters!'
        msg_alert_password = 'Password must be between 4 and 20 characters!'
        msg_alert_privacy_policy = 'Warning: You must agree to the Privacy Policy!'

        try:
            # self.browser.find_element(By.XPATH, alert_firstname)
            assert msg_alert_firstname in self.browser.page_source, f'Not present msg {msg_alert_firstname}'
            assert msg_alert_lastname in self.browser.page_source, f'Not present msg {msg_alert_lastname}'
            assert msg_alert_email in self.browser.page_source, f'Not present msg {msg_alert_email}'
            assert msg_alert_telephone in self.browser.page_source, f'Not present msg {msg_alert_telephone}'
            assert msg_alert_password in self.browser.page_source, f'Not present msg {msg_alert_password}'
            assert msg_alert_privacy_policy in self.browser.page_source, f'Not present msg {msg_alert_privacy_policy}'

            print('Alert found')
        except NoSuchElementException:
            assert False, "No alert messages were found on this page."
