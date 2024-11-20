from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # Chrome browser configuration:
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # Firefox browser configuration:
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # headless configuration for chrome:

    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window--size=1920*1080')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # firefox headless
    #
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window--size=1920*1080')
    # service = Service(GeckoDriverManager().install())
    # context.driver = webdriver.Firefox(
    #     options=options,
    #     service=service
    # )

    # browserstack
    #
    # bs_user = 'ilarievilbrun_vaPklz'
    # bs_key = '5ABFyZyFfdFgLfGyY3Av'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '11',
    #     'browserName': 'chrome',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    #

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
