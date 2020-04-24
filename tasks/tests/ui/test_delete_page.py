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
        page = DeletePage(browser, browser.current_url)
        page.should_be_correct_delete_page(name)

    def test_check_cancel_button_is_work_correct(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.delete_button_should_lead_to_delete_page()
        page = DeletePage(browser, browser.current_url)
        page.cancel_button_should_lead_to_main_page()
        page.browser.back()

    @pytest.mark.django_db
    def test_check_correct_delete_operations_and_message(self, browser):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.delete_button_should_lead_to_delete_page()
        page = DeletePage(browser, browser.current_url)
        page.click_confirm_delete_tasks()
        page.should_be_correct_success_message()
        page.should_be_no_elements_on_db_or_main_page_after_delete_task()
