from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then


@given('open Reelly Sign In page')
def signin_page(context):
    context.app.signin_page.signin_page()


@when('user logs in')
def log_in(context):
    context.app.signin_page.log_in()


@then('click on settings')
def click_settings_btn(context):
    context.app.welcome_page.click_settings_btn()


@then('click on User Guide option')
def click_user_guide_option(context):
    context.app.settings_page.click_user_guide_option()


@then('verify the right page opens')
def verify_right_page(context):
    context.app.settings_page.verify_right_page()


@then('verify all lesson videos contain titles')
def verify_lessons(context):
    context.app.settings_page.verify_lessons()
