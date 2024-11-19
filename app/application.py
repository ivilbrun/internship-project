from pages.base_page import Page
from pages.Signin_page import Signin
from pages.settings_page import Settings
from pages.welcome_page import Welcome


class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)

        self.signin_page = Signin(driver)
        self.settings_page = Settings(driver)
        self.welcome_page = Welcome(driver)



