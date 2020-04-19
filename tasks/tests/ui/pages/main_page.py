from .base_page import BasePage
from .locators import MainPageLocators
from tasks.models import Task


class MainPage(BasePage):
    def task_count_on_page_should_be_equal_task_count_in_database(self):
        task_count_on_page = self.get_element_text(
            MainPageLocators.TASK_COUNT
        )
        task_count_in_database = Task.objects.all().count()
        print(task_count_on_page)
        print(task_count_in_database)
        assert int(task_count_on_page) == task_count_in_database, \
            'Number of tasks on page is not equal in the database'

    def should_be_main_page(self):
        self.should_be_main_url()
        self.should_be_input_title()
        self.should_be_input_description()
        self.should_be_create_task_button()
        self.should_be_task_count()

    def create_task_with_title_and_description(self, task_name, task_descr):
        self.write_task_title(task_name)
        self.write_task_description(task_descr)
        self.click_create_task_button()

    def check_success_message_about_create_task(self):
        self.should_be_success_message_about_created_new_task()
        self.should_be_correct_success_message_text_about_created_new_task()

    def check_created_task_on_page(self):
        pass

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

    def should_be_no_tasks_on_page(self):
        assert self.is_not_element_present(
            *MainPageLocators.TASK_ROW
        ), 'Task is presented, but should not be'

    def should_be_tasks_on_page(self):
        assert self.is_element_present(
            *MainPageLocators.TASK_ROW
        ), 'Task is not presented, but should be'

    def write_task_title(self, task_name):
        self.browser.find_element(
            *MainPageLocators.INPUT_TITLE
        ).send_keys(task_name)

    def write_task_description(self, task_description):
        self.browser.find_element(
            *MainPageLocators.INPUT_DESCRIPTION
        ).send_keys(task_description)

    def click_create_task_button(self):
        self.browser.find_element(
            *MainPageLocators.CREATE_TASK_BUTTON
        ).click()

    def should_be_success_message_about_created_new_task(self):
        assert self.browser.find_element(
            *MainPageLocators.SUCCESS_MESSAGE
        ), 'Success message is not presented, but should be'

    def should_be_correct_success_message_text_about_created_new_task(self):
        assert 'Задача успешно создана!' == self.get_element_text(
            MainPageLocators.SUCCESS_MESSAGE
        ), 'Success message is not correct'

    def should_success_message_disappear(self):
        assert self.is_disappeared(
            *MainPageLocators.SUCCESS_MESSAGE
        ), "Success message is not disappeared"
