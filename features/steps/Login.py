import time
from behave import given, when, then, step, use_step_matcher, use_fixture

use_step_matcher('parse')


@given(u'User navigates to login page')
def step_impl(context):
    pass


@when(u'User enters valid email address {username} into email field')
def step_impl(context, username):
    pass


@when(u'User enters invalid email address into email field')
def step_impl(context):
    pass


@when(u'User dont enter email address into email field')
def step_impl(context):
    pass


@step(u'User enters valid password {password} into password field')
def step_impl(context, password):
    pass


@step(u'User enters invalid password "1234567890" into password field')
def step_impl(context):
    pass


@when(u'User dont enter password into password field')
def step_impl(context):
    pass


@step(u'User clicks on Login button')
def step_impl(context):
    pass


@then(u'User should get successfully logged in')
def step_impl(context):
    pass



@then(u'User should get a proper warning message about credentials mismatch')
def step_impl(context):
    pass



