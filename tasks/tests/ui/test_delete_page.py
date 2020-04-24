from .test_main_page import get_fake_name_and_email
from .pages.delete_page import DeletePage
from .pages.main_page import MainPage
import pytest


class TestCheckDeletePage:
    @pytest.fixture(scope="function", autouse=True)
    def setup_method(self, browser):
        link = 'http://127.0.0.1:8000/'
        self.page = MainPage(browser, link)
        self.page.open()

    def teardown_method(self):
        self.page.click_confirm_delete_tasks()

    @pytest.mark.django_db
    def test_check_delete_page_is_correct(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.delete_button_should_lead_to_delete_page()
        self.delete_page = DeletePage(browser, browser.current_url)
        self.delete_page.should_be_correct_delete_page(name)

    def test_check_cancel_button_is_work_correct(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.delete_button_should_lead_to_delete_page()
        self.delete_page = DeletePage(browser, browser.current_url)
        self.delete_page.cancel_button_should_lead_to_main_page()
        self.delete_page.browser.back()

    @pytest.mark.django_db
    def test_check_correct_delete_operations_and_message(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.delete_button_should_lead_to_delete_page()
        self.delete_page = DeletePage(browser, browser.current_url)
        self.delete_page.click_confirm_delete_tasks()
        self.delete_page.should_be_correct_success_message()
        self.delete_page.should_be_no_elements_on_db_or_main_page_after_del()

    @pytest.mark.xfail(
        reasen='Should be success message visible(Negative check)')
    def test_success_message_after_delete_should_be_visible(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.delete_button_should_lead_to_delete_page()
        self.delete_page = DeletePage(browser, browser.current_url)
        self.delete_page.click_confirm_delete_tasks()
        self.page.should_not_be_success_message()

    @pytest.mark.xfail(
        reason="Successful message should not fade(Negative check)")
    def test_success_message_disappeared_after_delete_task(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.delete_button_should_lead_to_delete_page()
        self.delete_page = DeletePage(browser, browser.current_url)
        self.delete_page.click_confirm_delete_tasks()
        self.page.should_success_message_disappear()

    def test_user_can_go_to_main_page_from_delete_page(self):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.delete_button_should_lead_to_delete_page()
        self.page.go_to_main_page()
        self.page.should_be_main_page()
        self.page.browser.back()

    @pytest.mark.xfail(reasen='Should be danger message(Negative check)')
    def test_danger_message_on_page_not_present(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.delete_button_should_lead_to_delete_page()
        self.delete_page = DeletePage(browser, browser.current_url)
        self.delete_page.should_not_be_danger_message()

    @pytest.mark.xfail(reasen='Should be question message(Negative check)')
    def test_question_message_on_page_not_present(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.delete_button_should_lead_to_delete_page()
        self.delete_page = DeletePage(browser, browser.current_url)
        self.delete_page.should_not_be_question_message()
