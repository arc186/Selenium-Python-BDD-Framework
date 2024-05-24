from behave import *
from features.page.homepage import Homepage
from utilities import emailgenerator

@given('open login page')
def step_impl(context):
    home_page = Homepage(context.driver)
    home_page.click_on_my_account()
    context.login_page = home_page.click_on_login_option()

@when('enter valid email_address as "{email}" and valid password as "{password}"')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)

@when('click on login button')
def step_impl(context):
    context.account_page = context.login_page.login_button()

@then('should logging successfully')
def step_impl(context):
    assert context.account_page.display_status()

@when('enter invalid email address and invalid password "{password}"')
def step_impl(context, password):
    invalid_email = emailgenerator.get_email_with_timestamp()
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)

@then('display proper warning message')
def step_impl(context):
    assert context.login_page.warning_message("Warning: No match for E-Mail Address and/or Password.")

@when('enter valid email address "{email}" and invalid password "{password}"')
def step_impl(context, email, password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)

@when('enter invalid email address and valid password "{password}"')
def step_impl(context, password):
    invalid_email = emailgenerator.get_email_with_timestamp()
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)

@when('not entering any credential details')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")

@when('enter valid email address "{email}" only')
def step_impl(context, email):
    context.login_page.enter_email_address(email)

@when('enter valid password "{password}" only')
def step_impl(context, password):
    context.login_page.enter_password(password)
