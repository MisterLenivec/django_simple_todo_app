from .test_main_page import get_fake_name_and_email
from .pages.main_page import MainPage
from .pages.update_page import UpdatePage
import pytest


class TestCheckUpdatePage:
    @pytest.fixture(scope="function", autouse=True)
    def setup_method(self, browser):
        link = 'http://127.0.0.1:8000/'
        self.page = MainPage(browser, link)
        self.page.open()

    def teardown_method(self):
        if self.page.should_be_tasks_on_page_for_delete():
            self.page.delete_button_should_lead_to_delete_page()
            self.page.click_confirm_delete_tasks()

    def test_user_can_go_to_main_page_from_update_page(self):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.edit_button_should_lead_to_edit_page()
        self.page.go_to_main_page()
        self.page.should_be_main_page()

    def test_check_update_page_url(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.edit_button_should_lead_to_edit_page()
        self.update_page = UpdatePage(browser, browser.current_url)
        self.update_page.should_be_update_page_url()
        self.update_page.browser.back()

    def test_check_update_page_is_correct(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.edit_button_should_lead_to_edit_page()
        self.update_page = UpdatePage(browser, browser.current_url)
        self.update_page.should_be_correct_delete_page()
        self.update_page.browser.back()

    @pytest.mark.django_db
    def test_check_task_attributes_on_update_is_correct(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.edit_button_should_lead_to_edit_page()
        self.update_page = UpdatePage(browser, browser.current_url)
        self.update_page.should_be_correct_task_attributes(name, email)
        self.update_page.browser.back()

    def test_cancel_button_should_lead_to_main_page(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.edit_button_should_lead_to_edit_page()
        self.update_page = UpdatePage(browser, browser.current_url)
        self.update_page.cancel_button_should_lead_to_main_page()

    def test_cancel_button_should_not_save_changes(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.edit_button_should_lead_to_edit_page()
        self.update_page = UpdatePage(browser, browser.current_url)
        second_name, second_email = get_fake_name_and_email()
        self.update_page.should_be_edit_input_title(second_name)
        self.update_page.cancel_button_should_lead_to_main_page()
        self.update_page.should_be_wrong_task_title(second_name)

    # @pytest.mark.xfail(reasen='Should be update message(Negative check)')
    # def test_update_message_on_update_page_is_not_present(self, browser):
    #     name, email = get_fake_name_and_email()
    #     self.page.create_task_with_title_and_description(name, email)
    #     self.page.edit_button_should_lead_to_edit_page()
    #     self.update_page = UpdatePage(browser, browser.current_url)
    #     self.update_page.should_not_be_update_message()
    #     self.update_page.browser.back()
