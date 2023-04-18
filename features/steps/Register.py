import time
from behave import given, when, then, step, use_step_matcher, use_fixture
from page_objects.home_page import HomePage
from page_objects.register_page import RegisterPage, RegisterPageAlerts

use_step_matcher('parse')


@given(u'User navigates to Register Account page')
def step_impl(context):
    context.browser.get(HomePage.url_home_page)
    context.home_page = HomePage(context.browser)
    context.home_page.my_account_drop_menu()
    context.home_page.select_register()


@when(u'User enters the details into below fields')
def step_impl(context):
    pass


@when(u'User dont enter any details into fields')
def step_impl(context):
    pass


@step(u'User selects Yes for Newsletter')
def step_impl(context):
    pass


@step(u'User selects Privacy Policy')
def step_impl(context):
    pass


@step(u'User clicks on Continue button')
def step_impl(context):
    pass


@then(u'User account should get created successfully')
def step_impl(context):
    pass


@then(u'User should get a proper warning about duplicate email')
def step_impl(context):
    pass


@then(u'User should get proper warning messages for every mandatory field')
def step_impl(context):
    pass
