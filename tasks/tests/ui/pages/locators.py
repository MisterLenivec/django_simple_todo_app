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
    TASK_ROW = (By.CLASS_NAME, 'task_row')
    TASK_NAME = (By.CLASS_NAME, 'task_name')
    EDIT_TASK = (By.CSS_SELECTOR, '.edit')
    DELETE_TASK = (By.CSS_SELECTOR, '.delete')


class DeletePageLocators:
    CONFIRM_DELETE = (By.CLASS_NAME, 'confirm_button')
    DANGER_MESSAGE = (By.CLASS_NAME, 'alert-danger')
    QUESTION_MESSAGE = (By.CSS_SELECTOR, 'p')
    QUESTION_TASK_TITLE = (By.CLASS_NAME, 'task')
    CANCEL_BUTTON = (By.CLASS_NAME, 'cancel_button')
    CONFIRM_DELETE_BUTTON = (By.CLASS_NAME, 'confirm_button')


class UpdatePageLocators:
    UPDATE_MESSAGE = (By.CLASS_NAME, 'alert-success')
    INPUT_TITLE = (By.ID, 'id_title')
    INPUT_DESCRIPTION = (By.ID, 'id_description')
    LABEL_FOR_ID_COMPLETE = (By.CLASS_NAME, 'form-check-label')
    CHECKBOX = (By.ID, 'id_complete')
    TASK_CREATED = (By.ID, 'task_created')
    TASK_UPDATED = (By.ID, 'task_updated')
    TASK_CREATED_DATE = (By.ID, 'task_created_date')
    TASK_UPDATED_DATE = (By.ID, 'task_updated_date')
    CANCEL_BUTTON = (By.CLASS_NAME, 'cancel_button')
    CONFIRM_UPDATE_BUTTON = (By.CLASS_NAME, 'confirm_button')
