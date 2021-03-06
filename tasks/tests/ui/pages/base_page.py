from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):  # delete -  timeout=10
        self.browser = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_main_page_link(self):
        assert self.is_element_present(
            *BasePageLocators.MAIN_PAGE
        ), "Login link is not presented"

    def go_to_main_page(self):
        link = self.browser.find_element(*BasePageLocators.MAIN_PAGE)
        link.click()

    def get_element_text(self, name):
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located(name))
        try:
            return str(self.browser.find_element(*name).text)
        except NoSuchElementException:
            return None

    # def is_element_present(self, how, what):
    #     try:
    #         self.browser.find_element(how, what)
    #     except NoSuchElementException:
    #         return False
    #     return True

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
