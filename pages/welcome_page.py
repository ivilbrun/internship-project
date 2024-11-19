from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Welcome(Page):
    settings_btn = (By.CSS_SELECTOR, '[href="/settings"]')

    def welcome(self):
        self.open_url('https://soft.reelly.io/')

    def click_settings_btn(self):
        self.click(*self.settings_btn)
        sleep(3)