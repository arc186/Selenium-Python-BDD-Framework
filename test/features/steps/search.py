from behave import *

from features.page.homepage import Homepage

@given('Navigate to home page')
def step_impl(context):
    context.home_page = Homepage(context.driver)
    assert context.home_page.check_home_page_title("Your Store")

@when('enter valid product "{product_name}" in search Box field')
def step_impl(context, product_name):
    context.home_page.search_product_field(product_name)

@when('click on search button')
def step_impl(context):
    context.search_page = context.home_page.search_click()

@then('valid product should be display on screen')
def step_impl(context):
    assert context.search_page.display_valid_product_status()

@when('enter invalid product "{product_name}" in search Box field')
def step_impl(context, product_name):
    context.home_page.search_product_field(product_name)

@when('dont enter anything on search box filed')
def step_impl(context):
    context.home_page.search_product_field("")

@then('proper error message should be display on screen')
def step_impl(context):
    assert context.search_page.product_error_status("There is no product that matches the search criteria.")