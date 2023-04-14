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
    context.register_page = RegisterPage(context.browser)
    table = context.table  # Obtiene la tabla de datos del contexto
    data = table.rows[0]  # Obtiene la primera fila de datos de la tabla

    # Llena los campos del formulario con los datos de la tabla
    firstname = data["firstName"]
    lastname = data["lastName"]
    email = data["email"]
    telephone = data["telephone"]
    password = data["password"]

    context.register_page.input_firstname(firstname)
    context.register_page.input_lastname(lastname)
    context.register_page.input_email(email)
    context.register_page.input_telephone(telephone)
    context.register_page.input_password(password)
    context.register_page.input_confirm_password(password)


@when(u'User dont enter any details into fields')
def step_impl(context):
    pass


@step(u'User selects Yes for Newsletter')
def step_impl(context):
    context.register_page = RegisterPage(context.browser)
    context.register_page.select_yes_newsletter()


@step(u'User selects Privacy Policy')
def step_impl(context):
    register_page = RegisterPage(context.browser)
    register_page.select_agree_privacy_policy()


@step(u'User clicks on Continue button')
def step_impl(context):
    register_page = RegisterPage(context.browser)
    register_page.submit_register()
    # pass


@then(u'User account should get created successfully')
def step_impl(context):
    pass


@then(u'User should get a proper warning about duplicate email')
def step_impl(context):
    pass


@then(u'User should get proper warning messages for every mandatory field')
def step_impl(context):
    context.register_page_alerts = RegisterPageAlerts(context.browser)
    context.register_page_alerts.msgs_alerts()


