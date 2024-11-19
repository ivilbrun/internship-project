from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Signin(Page):
    email_field = (By.ID, 'email-2')
    password_field = (By.ID, 'field')
    login_btn = (By.XPATH, "//a[contains(@class, 'login-button w-button')]")

    def signin_page(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def log_in(self):
        sleep(3)
        self.input_text('0120ilarievilbrun@gmail.com', *self.email_field)
        self.input_text('Ruth3630978@', *self.password_field)
        self.click(*self.login_btn)
        sleep(5)
