from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class Settings(Page):
    user_guide = (By.XPATH, "//a[@href='/user-guide'] //div[@class='setting-text']")
    first_iframe_locator = (By.CSS_SELECTOR, '[class="ditals-block"] [class="embedly-embed"]')
    second_iframe_locator = (By.ID, 'player')

    def click_user_guide_option(self):
        self.driver.find_element(By.XPATH, "//a[@href='/main-menu'] //div[@class='circle-gradient']").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(By.XPATH, "//a[@href='/user-guide'] //div[@class='icon-text-block-menu']").click()
        sleep(2)

    def verify_right_page(self):
        url = self.driver.current_url
        assert "user-guide" in url, f'Expected "user-guide" not in {url}'
        print('Verified right page is opened')

    def verify_lessons(self):
        first_iframe = self.find_element(*self.first_iframe_locator)
        self.driver.switch_to.frame(first_iframe)
        second_iframe = self.find_element(*self.second_iframe_locator)
        self.driver.switch_to.frame(second_iframe)

        title = self.find_element(By.CSS_SELECTOR, '[data-sessionlink="feature=player-title"]')
        assert "Full overview of Reelly platform" in title.text, f'Expected video title is not found in {title.text}'
        print('Verified all lesson videos contain titles')

