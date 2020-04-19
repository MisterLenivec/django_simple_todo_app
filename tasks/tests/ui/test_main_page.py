from .pages.main_page import MainPage
from faker import Faker
import pytest


class TestCheckMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://127.0.0.1:8000/'
        self.page = MainPage(browser, link)
        self.page = MainPage(browser, link)
        self.page.open()

    def test_user_can_go_to_main_page_from_main_page(self):
        self.page.should_be_main_page()
        self.page.go_to_main_page()

    # @pytest.mark.django_db
    # def test_comparison_of_the_number_of_tasks(self, browser):
    #     link = 'http://127.0.0.1:8000/'
    #     page = MainPage(browser, link)
    #     page.open()
    #     page.should_be_main_page()
    #     page.task_count_on_page_should_be_equal_task_count_in_database()

    @pytest.mark.xfail(reasen='Should be no task on page')
    def test_tasks_on_page_present(self):
        self.page.should_be_main_page()
        self.page.should_be_tasks_on_page()

    # @pytest.mark.django_db
    def test_create_tasks(self):
        self.page.should_be_main_page()
        # page.task_count_on_page_should_be_equal_task_count_in_database()
        self.page.should_be_no_tasks_on_page()
        f = Faker()
        name = f.name()
        email = f.email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.check_success_message_about_create_task()
        # page.task_count_on_page_should_be_equal_task_count_in_database()
        self.page.should_be_tasks_on_page()

    @pytest.mark.xfail(
        reason="Successful message should not fade(Negative check)")
    def test_message_disappeared_after_adding_product_to_basket(self):
        self.page.should_be_main_page()
        f = Faker()
        name = f.name()
        email = f.email()
        self.page.create_task_with_title_and_description(name, email)
        self.page.check_success_message_about_create_task()
        self.page.should_success_message_disappear()
