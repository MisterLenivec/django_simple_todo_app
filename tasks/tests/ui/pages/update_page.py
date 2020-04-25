from .base_page import BasePage
from .locators import MainPageLocators, UpdatePageLocators
from tasks.models import Task


class UpdatePage(BasePage):
    def should_be_correct_delete_page(self):
        self.should_be_update_message()
        self.should_be_correct_text_in_update_message()
        self.should_be_input_title_on_update_page()
        self.should_be_input_description_on_update_page()
        self.should_be_label_for_checkbox()
        self.should_be_correct_text_in_label_for_checkbox()
        self.should_be_checkbox_on_update_page()
        self.should_be_task_created_row()
        self.should_be_task_updated_row()
        self.should_be_task_created_date_row()
        self.should_be_task_updated_date_row()
        self.should_be_cancel_button_on_update_page()
        self.should_be_confirm_button_on_update_page()
        self.should_be_correct_text_cancel_button_on_update_page()
        self.should_be_correct_text_confirm_button_on_update_page()

    def should_be_correct_task_attributes(self, task_name, task_descr):
        self.should_be_correct_text_in_input_title(task_name)
        self.should_be_correct_text_in_input_description(task_descr)
        self.should_be_correct_text_in_input_title_on_db(task_name)
        self.should_be_correct_text_in_input_description_on_db(task_descr)
        self.should_be_not_selected_checkbox()

    def should_be_edit_task(self, task_name, task_descr):
        self.should_be_edit_input_title(task_name)
        self.should_be_edit_input_description(task_descr)
        self.should_be_select_checkbox()
        self.should_be_click_confirm_button_for_update_task()

    def check_success_message_about_update_task(self):
        self.should_be_update_success_message()
        self.should_be_correct_update_success_message_text()

    def should_be_correct_task_name_complete(self, task_name):
        self.should_be_task_name_complete()
        self.should_be_correct_update_text_in_task_title_in_main(task_name)

    def should_be_update_page_url(self):
        assert 'update_task' in self.browser.current_url, \
            "Update page url is not presented"

    def should_be_correct_update_task(self):
        self.should_be_correct_updated_input_title_on_db()
        self.should_be_correct_updated_input_description_on_db()
        self.should_be_correct_updated_checkbox_on_db()

    def should_be_update_message(self):
        assert self.is_element_present(
            *UpdatePageLocators.UPDATE_MESSAGE
        ), 'Update message on update page is not presented, but should be'

    def should_be_correct_text_in_update_message(self):
        assert 'Редактировать' == self.get_element_text(
            UpdatePageLocators.UPDATE_MESSAGE
        ), 'Text in update message is not correct, but should be'

    def should_be_input_title_on_update_page(self):
        assert self.is_element_present(
            *UpdatePageLocators.INPUT_TITLE
        ), 'Input title on update page is not presented'

    def should_be_input_description_on_update_page(self):
        assert self.is_element_present(
            *UpdatePageLocators.INPUT_DESCRIPTION
        ), 'Input description on update page is not presented'

    def should_be_label_for_checkbox(self):
        assert self.is_element_present(
            *UpdatePageLocators.LABEL_FOR_ID_COMPLETE
        ), 'Label for checkbox on update page is not presented, but should be'

    def should_be_correct_text_in_label_for_checkbox(self):
        assert 'Задача выполнена?' == self.get_element_text(
            UpdatePageLocators.LABEL_FOR_ID_COMPLETE
        ), 'Label text for checkbox on update page is not correct, ' \
           'but should be'

    def should_be_checkbox_on_update_page(self):
        assert self.is_element_present(
            *UpdatePageLocators.CHECKBOX
        ), 'Checkbox on update page is not present, but should be'

    def should_be_task_created_row(self):
        assert self.is_element_present(
            *UpdatePageLocators.TASK_CREATED
        ), 'Task created text on update page is not present, but should be'

    def should_be_task_updated_row(self):
        assert self.is_element_present(
            *UpdatePageLocators.TASK_UPDATED
        ), 'Task updated text on update page is not present, but should be'

    def should_be_task_created_date_row(self):
        assert self.is_element_present(
            *UpdatePageLocators.TASK_CREATED_DATE
        ), 'Task created date on update page is not present, but should be'

    def should_be_task_updated_date_row(self):
        assert self.is_element_present(
            *UpdatePageLocators.TASK_UPDATED_DATE
        ), 'Task updated date on update page is not present, but should be'

    def should_be_cancel_button_on_update_page(self):
        assert self.is_element_present(
            *UpdatePageLocators.CANCEL_BUTTON
        ), 'Cancel button on update page is not present, but should be'

    def should_be_confirm_button_on_update_page(self):
        assert self.is_element_present(
            *UpdatePageLocators.CONFIRM_UPDATE_BUTTON
        ), 'Confirm button on update page is not present, but should be'

    def should_be_correct_text_cancel_button_on_update_page(self):
        assert 'Отмена' == self.get_element_text(
            UpdatePageLocators.CANCEL_BUTTON
        ), 'Cancel button text on update page is not correct, but should be'

    def should_be_correct_text_confirm_button_on_update_page(self):
        assert 'Обновить' == self.browser.find_element(
            *UpdatePageLocators.CONFIRM_UPDATE_BUTTON
        ).get_attribute('value'), \
            'Confirm button text on update page is not correct, but should be'

    def should_be_correct_text_in_input_title(self, task_name):
        assert task_name == self.browser.find_element(
            *UpdatePageLocators.INPUT_TITLE
        ).get_attribute('value'), \
            'Text in input title is not correct on update page, but should be'

    def should_be_correct_text_in_input_description(self, task_descr):
        assert task_descr == self.get_element_text(
            UpdatePageLocators.INPUT_DESCRIPTION
        ), 'Text in input description on update page is not correct, ' \
           'but should be'

    @staticmethod
    def should_be_correct_text_in_input_title_on_db(task_name):
        assert task_name == Task.objects.first().title, \
            'Text in input title is not correct on update page, but should be'

    @staticmethod
    def should_be_correct_text_in_input_description_on_db(task_descr):
        assert task_descr == Task.objects.first().description, \
            'Text in input description on update page is not correct, ' \
            'but should be'

    def should_be_not_selected_checkbox(self):
        assert self.browser.find_element(
            *UpdatePageLocators.CHECKBOX
        ).get_attribute("checked") is None, \
            'Checkbox is selected, but not should be'

    def should_be_selected_checkbox(self):
        assert self.browser.find_element(
            *UpdatePageLocators.CHECKBOX
        ).get_attribute("checked") == "true", \
            'Checkbox is not selected, but should be'

    def cancel_button_should_lead_to_main_page(self):
        self.browser.find_element(
            *UpdatePageLocators.CANCEL_BUTTON
        ).click()
        assert 'http://127.0.0.1:8000/' == self.browser.current_url, \
            'Cancel button not lead to main page'

    def should_be_edit_input_title(self, task_name):
        title = self.browser.find_element(
            *UpdatePageLocators.INPUT_TITLE
        )
        title.clear()
        title.send_keys(task_name)
        assert title.get_attribute('value') == task_name, \
            'Edited text in input title is not correct on update page, ' \
            'but should be'

    def should_be_edit_input_description(self, task_descr):
        """
        send keys to description
        """
        description = self.browser.find_element(
            *UpdatePageLocators.INPUT_DESCRIPTION
        )
        description.clear()
        description.send_keys(task_descr)

    def should_be_select_checkbox(self):
        checkbox = self.browser.find_element(
            *UpdatePageLocators.CHECKBOX
        )
        checkbox.click()
        assert checkbox.get_attribute('checked') == 'true', \
            'Checkbox is not selected, but should be'

    def should_be_click_confirm_button_for_update_task(self):
        self.browser.find_element(
            *UpdatePageLocators.CONFIRM_UPDATE_BUTTON
        ).click()
        assert 'http://127.0.0.1:8000/' == self.browser.current_url, \
            'Confirm button not lead to main page, but should be'

    def should_be_update_success_message(self):
        assert self.is_element_present(
            *MainPageLocators.SUCCESS_MESSAGE
        ), 'Success message about update task is not presented, but should be'

    def should_not_be_update_success_message(self):
        assert self.is_not_element_present(
            *MainPageLocators.SUCCESS_MESSAGE
        ), 'Success message about update task is not presented, ' \
           'but should be negative check'

    def should_be_correct_update_success_message_text(self):
        assert 'Задача успешно обновлена!' == self.get_element_text(
            MainPageLocators.SUCCESS_MESSAGE
        ), 'Success message text about update task is not correct'

    def should_be_task_name_complete(self):
        assert self.is_element_present(
            *MainPageLocators.TASK_NAME_COMPLETE
        ), 'Task name complete is not presented, but should be'

    def should_not_be_task_name_complete(self):
        assert self.is_not_element_present(
            *MainPageLocators.TASK_NAME_COMPLETE
        ), 'Task name complete is presented, but it passed if not'

    def should_be_correct_update_text_in_task_title_in_main(self, task_name):
        assert task_name == self.get_element_text(
            MainPageLocators.TASK_NAME_COMPLETE
        ), 'Task title (completed) text is not correct, but should be'

    def should_be_correct_updated_input_title_on_db(self):
        assert Task.objects.first().title == self.browser.find_element(
            *UpdatePageLocators.INPUT_TITLE
        ).get_attribute('value'), 'Updated text in input title is not equal ' \
                                  'title text in database, but should be'

    def should_be_correct_updated_input_description_on_db(self):
        assert Task.objects.first().description == self.get_element_text(
            UpdatePageLocators.INPUT_DESCRIPTION
        ), 'Updated text in input description is not equal description text ' \
           'in database, but should be'

    def should_be_correct_updated_checkbox_on_db(self):
        db_checkbox = str(Task.objects.first().complete).lower()
        page_checkbox = str(self.browser.find_element(
            *UpdatePageLocators.CHECKBOX
        ).get_attribute('checked'))
        assert db_checkbox == page_checkbox, 'Updated checkbox on database ' \
            'not equal checkbox on page, but should be'

    def should_be_wrong_task_title(self, task_name):
        assert self.browser.find_element(
            *MainPageLocators.TASK_NAME
        ).get_attribute('value') != task_name, \
            'Task title is correct, but should not be'

    def should_be_correct_task_title(self, task_name):
        assert self.browser.find_element(
            *MainPageLocators.TASK_NAME
        ).get_attribute('value') == task_name, \
            'Task title is not correct, but should be'

    def should_not_be_update_message(self):
        assert self.is_not_element_present(
            *UpdatePageLocators.UPDATE_MESSAGE
        ), 'Update message on update page is presented, but should not be'
