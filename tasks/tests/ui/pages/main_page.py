from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import MainPageLocators
from tasks.models import Task


class MainPage(BasePage):
    def get_element_text(self, name):
        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(name))
        try:
            return str(self.browser.find_element(*name).text)
        except NoSuchElementException:
            return None

    def task_count_on_page_should_be_equal_task_count_in_database(self):
        task_count_on_page = self.get_element_text(
            MainPageLocators.TASK_COUNT
        )
        task_count_in_database = Task.objects.all().count()
        assert int(task_count_on_page) == task_count_in_database, \
            'Number of tasks on page is not equal in the database'

    def should_be_main_page(self):
        self.should_be_main_url()
        self.should_be_input_title()
        self.should_be_input_description()
        self.should_be_create_task_button()
        self.should_be_task_count()

    def should_be_main_url(self):
        assert "http://127.0.0.1:8000/" == self.browser.current_url, \
            "Main url is not presented"

    def should_be_input_title(self):
        assert self.is_element_present(
            *MainPageLocators.INPUT_TITLE
        ), 'Input title is not present'

    def should_be_input_description(self):
        assert self.is_element_present(
            *MainPageLocators.INPUT_DESCRIPTION
        ), 'Input description is not present'

    def should_be_create_task_button(self):
        assert self.is_element_present(
            *MainPageLocators.CREATE_TASK_BUTTON
        ), 'Create task button is not present'

    def should_be_task_count(self):
        assert self.is_element_present(
            *MainPageLocators.TASK_COUNT_STRING
        ), 'Count tasks string is not present'
