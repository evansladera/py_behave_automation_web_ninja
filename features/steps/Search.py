import time
from behave import given, when, then, step, use_step_matcher

use_step_matcher('parse')


@given(u'User opens the Application')
def step_impl(context):
    pass


@when(u'User enters valid product "HP" into Search box field')
def step_impl(context):
    pass


@when(u'User enters invalid product "Honda" into Search box field')
def step_impl(context):
    pass


@when(u'User dont enter any product name into Search box field')
def step_impl(context):
    pass


@step(u'User clicks on Search button')
def step_impl(context):
    pass


@then(u'User should get valid product displayed in search results')
def step_impl(context):
    pass


@then(u'User should get a message about no product matching')
def step_impl(context):
    pass
