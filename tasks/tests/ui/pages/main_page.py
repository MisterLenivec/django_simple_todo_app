from .base_page import BasePage
from .locators import MainPageLocators, DeletePageLocators
from tasks.models import Task
from selenium.common.exceptions import NoSuchElementException


class MainPage(BasePage):
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

    def create_task_with_title_and_description(self, task_name, task_descr):
        self.write_task_title(task_name)
        self.write_task_description(task_descr)
        self.click_create_task_button()

    def check_success_message_about_create_task(self):
        self.should_be_success_message_about_created_new_task()
        self.should_be_correct_success_message_text_about_created_new_task()

    def check_edit_button_is_present_with_correct_text(self):
        self.should_be_edit_button_in_task_row()
        self.should_be_correct_text_in_edit_button()

    def check_delete_button_is_present_with_correct_text(self):
        self.should_be_delete_button_in_task_row()
        self.should_be_correct_text_in_delete_button()

    def should_be_correct_task_name_and_description(self, title, descr):
        self.should_be_correct_task_name(title)
        self.create_task_title_should_be_correct_on_db(title)
        self.create_task_description_should_be_correct_on_db(descr)

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
        ), 'Success message is not disappeared'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *MainPageLocators.SUCCESS_MESSAGE
        ), 'Success message is presented, but should not be'

    def check_number_of_created_task_on_page(self):
        tasks_on_page = self.browser.find_elements(
            *MainPageLocators.TASK_ROW
        )
        task_count_on_page = self.get_element_text(
            MainPageLocators.TASK_COUNT
        )
        assert len(tasks_on_page) == int(task_count_on_page), \
            'Tasks on page not equal task counter'

    def should_be_correct_task_name(self, task_name):
        assert self.get_element_text(
            MainPageLocators.TASK_NAME
        ) == task_name, 'Task name not equal created task name'

    def should_be_edit_button_in_task_row(self):
        assert self.is_element_present(
            *MainPageLocators.EDIT_TASK
        ), 'Edit task button is not presented, but should be'

    def should_be_delete_button_in_task_row(self):
        assert self.is_element_present(
            *MainPageLocators.DELETE_TASK
        ), 'Delete task button is not presented, but should be'

    def should_be_correct_text_in_edit_button(self):
        assert self.get_element_text(
            MainPageLocators.EDIT_TASK
        ) == 'Изменить', 'Edit button text is not correct, but should be'

    def should_be_correct_text_in_delete_button(self):
        assert self.get_element_text(
            MainPageLocators.DELETE_TASK
        ) == 'Удалить', 'Delete button text is not correct, but should be'

    def edit_button_should_lead_to_edit_page(self):
        self.browser.find_element(
            *MainPageLocators.EDIT_TASK
        ).click()
        assert 'update_task' in self.browser.current_url, \
            'Current url is not an edit task page'

    def delete_button_should_lead_to_delete_page(self):
        self.browser.find_element(
            *MainPageLocators.DELETE_TASK
        ).click()
        assert 'delete_task' in self.browser.current_url, \
            'Current url is not an delete task page'

    def click_confirm_delete_tasks(self):
        try:
            self.browser.find_element(
                *DeletePageLocators.CONFIRM_DELETE
            ).click(), 'We\'re not on delete page or task is not present'
        except NoSuchElementException:
            pass

    def should_be_tasks_on_page_for_delete(self):  # refactor this later
        try:
            self.browser.find_element(*MainPageLocators.TASK_ROW)
            return True
        except NoSuchElementException:
            return False

    @staticmethod
    def create_task_title_should_be_correct_on_db(task_name):
        assert task_name == Task.objects.first().title, \
            'Task name on db not equal created task name'

    @staticmethod
    def create_task_description_should_be_correct_on_db(task_descr):
        assert task_descr == Task.objects.first().description, \
            'Task name on db not equal created task name'
