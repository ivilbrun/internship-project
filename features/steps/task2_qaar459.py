from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then


@given('open Reelly main page')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io')


@when('user logs in')
def log_in(context):
    sleep(5)
    context.driver.find_element(By.ID, 'email-2').send_keys('0120ilarievilbrun@gmail.com')
    context.driver.find_element(By.ID, 'field').send_keys('Ruth3630978@')
    context.driver.find_element(By.XPATH, "//a[contains(@class, 'login-button w-button')]").click()
    sleep(3)


@then('click on settings')
def click_settings(context):
    context.driver.find_element(By.CSS_SELECTOR, '[href="/settings"]').click()
    sleep(3)


@then('click on User Guide option')
def click_user_guide_option(context):
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    context.driver.find_element(By.XPATH, "//a[@href='/user-guide'] //div[@class='setting-text']").click()
    sleep(2)


@then('verify the right page opens')
def verify_right_page(context):
    url = context.driver.current_url
    assert "user-guide" in url, f'Expected "user-guide" not in {url}'
    print('Verified right page is opened')


@then('verify all lesson videos contain titles')
def verify_lessons(context):
    first_iframe_locator = (By.CSS_SELECTOR, '[class="ditals-block"] [class="embedly-embed"]')
    second_iframe_locator = (By.ID, 'player')

    first_iframe = context.driver.find_element(*first_iframe_locator)
    context.driver.switch_to.frame(first_iframe)
    second_iframe = context.driver.find_element(*second_iframe_locator)
    context.driver.switch_to.frame(second_iframe)

    title = context.driver.find_element(By.CSS_SELECTOR, '[data-sessionlink="feature=player-title"]')
    assert "Full overview of Reelly platform" in title.text, f'Expected video title is not found in {title.text}'
    print('Verified all lesson videos contain titles')
