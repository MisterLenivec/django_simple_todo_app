from .pages.main_page import MainPage
from faker import Faker
import pytest


def get_fake_name_and_email():
    f = Faker()
    name = f.name()
    email = f.email()
    return name, email


class TestCheckMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup_method(self, browser):
        link = 'http://127.0.0.1:8000/'
        self.page = MainPage(browser, link)
        self.page.open()

    def teardown_method(self):
        if self.page.should_be_tasks_on_page_for_delete():
            self.page.delete_button_should_lead_to_delete_page()
            self.page.click_confirm_delete_tasks()

    def test_main_page_link_is_present(self):
        self.page.should_be_main_page_link()

    def test_should_be_main_page(self):
        self.page.should_be_main_page()

    def test_user_can_go_to_main_page_from_main_page(self):
        self.page.go_to_main_page()
        self.page.should_be_main_page()

    # @pytest.mark.django_db
    # def test_comparison_of_the_number_of_tasks(self, browser):
    #     page.task_count_on_page_should_be_equal_task_count_in_database()

    @pytest.mark.xfail(reasen='Should be no task on page')
    def test_tasks_on_page_present(self):
        self.page.should_be_tasks_on_page()

    def test_tasks_on_page_not_present(self):
        self.page.should_be_no_tasks_on_page()

    # @pytest.mark.django_db
    def test_can_create_tasks(self):
        # page.task_count_on_page_should_be_equal_task_count_in_database()
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        # page.task_count_on_page_should_be_equal_task_count_in_database()
        self.page.should_be_tasks_on_page()

    def test_should_see_correct_success_message_after_create_task(self):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.check_success_message_about_create_task()

    def test_should_be_task_on_page_after_create(self):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.should_be_tasks_on_page()

    def test_cant_see_success_message(self):
        self.page.should_not_be_success_message()

    @pytest.mark.xfail(
        reason="Successful message should not fade(Negative check)")
    def test_message_disappeared_after_adding_product_to_basket(self):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.check_success_message_about_create_task()
        self.page.should_success_message_disappear()

    @pytest.mark.xfail(
        reason="Successful message should be visible(Negative check)")
    def test_message_not_visible_after_adding_product_to_basket(self):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.should_not_be_success_message()

    def test_number_of_tasks_is_equal_task_counter(self):
        self.page.check_number_of_created_task_on_page()

    def test_task_is_correct(self):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.should_be_correct_task_name(name)
        self.page.check_edit_button_is_present_with_correct_text()
        self.page.check_delete_button_is_present_with_correct_text()
        self.page.edit_button_should_lead_to_edit_page()
        self.page.go_to_main_page()

    def test_task_edit_button_is_work_correct(self):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.edit_button_should_lead_to_edit_page()
        self.page.go_to_main_page()

    def test_task_delete_button_is_work_correct(self):
        name, email = get_fake_name_and_email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.delete_button_should_lead_to_delete_page()
        self.page.go_to_main_page()
