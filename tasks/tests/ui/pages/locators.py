from selenium.webdriver.common.by import By


class BasePageLocators:
    MAIN_PAGE = (By.CLASS_NAME, 'leniva')


class MainPageLocators:
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'alert-success')
    INPUT_TITLE = (By.ID, 'id_title')
    INPUT_DESCRIPTION = (By.ID, 'id_description')
    CREATE_TASK_BUTTON = (By.NAME, 'create_task')
    TASK_COUNT_STRING = (By.CLASS_NAME, 'task_count_string')
    TASK_COUNT = (By.CLASS_NAME, 'task_count')