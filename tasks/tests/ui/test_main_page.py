from .pages.main_page import MainPage
import pytest


def test_user_can_go_to_main_page_from_main_page(browser):
    link = 'http://127.0.0.1:8000/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_main_page()
    page.go_to_main_page()


@pytest.mark.django_db
def test_comparison_of_the_number_of_tasks(browser):
    link = 'http://127.0.0.1:8000/'
    page = MainPage(browser, link)
    page.open()
    page.should_be_main_page()
    page.task_count_on_page_should_be_equal_task_count_in_database()
