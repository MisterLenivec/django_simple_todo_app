from .base_page import BasePage
from .locators import MainPageLocators, DeletePageLocators
from tasks.models import Task
from selenium.common.exceptions import NoSuchElementException


class DeletePage(BasePage):
    def should_be_correct_delete_page(self, task_name):
        self.should_be_danger_message()
        self.should_be_correct_text_in_danger_message()
        self.should_be_question_message()
        self.should_be_correct_text_in_question_message(task_name)
        self.should_be_correct_task_title_in_question_message()
        self.should_be_cancel_button_on_delete_page()
        self.should_be_confirm_delete_button_on_delete_page()
        self.should_be_correct_text_in_cancel_button()
        self.should_be_correct_text_in_confirm_delete_button()

    def should_be_correct_success_message(self):
        self.should_be_success_message_on_main_page_after_delete_task()
        self.should_be_correct_success_message_text_about_delete_task()

    def should_be_no_elements_on_db_or_main_page_after_del(self):
        self.should_be_no_task_on_main_page_after_delete()
        self.should_be_no_task_on_db_after_delete()

    def should_be_danger_message(self):
        assert self.is_element_present(
            *DeletePageLocators.DANGER_MESSAGE
        ), 'Danger message on delete page is not presented, but should be'

    def should_not_be_danger_message(self):
        assert self.is_not_element_present(
            *DeletePageLocators.DANGER_MESSAGE
        ), 'Danger message on delete page is not presented, but should be'

    def should_be_correct_text_in_danger_message(self):
        assert 'Удалить задачу' == self.get_element_text(
            DeletePageLocators.DANGER_MESSAGE
        ), 'Text in danger message is not correct, but should be'

    def should_be_question_message(self):
        assert self.is_element_present(
            *DeletePageLocators.QUESTION_MESSAGE
        ), 'Question message on delete page is not presented, but should be'

    def should_not_be_question_message(self):
        assert self.is_not_element_present(
            *DeletePageLocators.QUESTION_MESSAGE
        ), 'Question message on delete page is not presented, but should be'

    def should_be_correct_text_in_question_message(self, task_name):
        assert f"Вы уверены что хотите удалить '{task_name}'?" == \
               self.get_element_text(DeletePageLocators.QUESTION_MESSAGE), \
            'Question message is not correct'

    def should_be_correct_task_title_in_question_message(self):
        assert Task.objects.first().title in self.get_element_text(
            DeletePageLocators.QUESTION_MESSAGE
        ), 'Task title in db not equal task title in question message delete'

    def should_be_cancel_button_on_delete_page(self):
        assert self.is_element_present(
            *DeletePageLocators.CANCEL_BUTTON
        ), 'Cancel button is not presented, but should be'

    def should_be_confirm_delete_button_on_delete_page(self):
        assert self.is_element_present(
            *DeletePageLocators.CONFIRM_DELETE_BUTTON
        ), 'Confirm delete task button is not presented, but should be'

    def should_be_correct_text_in_cancel_button(self):
        assert self.get_element_text(
            DeletePageLocators.CANCEL_BUTTON
        ) == 'Отмена', 'Cancel button text is not correct, but should be'

    def should_be_correct_text_in_confirm_delete_button(self):
        assert self.browser.find_element(
            *DeletePageLocators.CONFIRM_DELETE_BUTTON
        ).get_attribute('value') == 'Подтвердить', \
            'Confirm delete button text is not correct, but should be'

    def cancel_button_should_lead_to_main_page(self):
        self.browser.find_element(
            *DeletePageLocators.CANCEL_BUTTON
        ).click()
        assert "http://127.0.0.1:8000/" == self.browser.current_url, \
            "Main url is not presented"

    def click_confirm_delete_tasks(self):
        try:
            self.browser.find_element(
                *DeletePageLocators.CONFIRM_DELETE
            ).click(), 'We\'re not on delete page or task is not present'
        except NoSuchElementException:
            pass

    def should_be_success_message_on_main_page_after_delete_task(self):
        assert self.browser.find_element(
            *MainPageLocators.SUCCESS_MESSAGE
        ), 'Success message about delete task is not presented, but should be'

    def should_be_correct_success_message_text_about_delete_task(self):
        assert 'Задача удалена!' == self.get_element_text(
            MainPageLocators.SUCCESS_MESSAGE
        ), 'Success message about delete task is not correct'

    def should_be_no_task_on_main_page_after_delete(self):
        assert self.is_not_element_present(
            *MainPageLocators.TASK_ROW
        ), 'Task is presented, but should not be'

    @staticmethod
    def should_be_no_task_on_db_after_delete():
        assert Task.objects.all().count() == 0, \
            'Tasks on db not equal 0'
