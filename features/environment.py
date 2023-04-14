import time

from selenium import webdriver
from behave import use_fixture, fixture
from selenium.webdriver.chrome.options import Options
from page_objects.home_page import HomePage

BEHAVE_TIMEOUT = 60


@fixture
def setup(context):
    context.opt_browser = Options()
    # context.opt_browser.add_argument('--headless')
    context.browser = webdriver.Chrome(options=context.opt_browser)

    context.browser.maximize_window()
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    yield context.browser


# def before_feature(context, feature):
#     use_fixture(setup, context)
#     # context.browser.get(HomePage.url_home_page)

def before_scenario(context, scenario):
    use_fixture(setup, context)


def after_scenario(context, scenario):
    context.browser.quit()
    time.sleep(2)


# def after_feature(context, feature):
#     context.browser.quit()
