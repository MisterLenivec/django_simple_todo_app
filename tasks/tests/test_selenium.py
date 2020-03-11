from django.test import TestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class SeleniumTests(TestCase):

    def test_task_app_with_selenium(self):
        for driver in [webdriver.Chrome(), webdriver.Firefox()]:
            self.browser = driver
            self.browser.implicitly_wait(5)
            self.browser.get('http://127.0.0.1:8000/')

            title_val = 'Selenium test value'
            desc_val = 'Selenium desc value'
            cards_val = ''

            try:
                """
                Number of cards from string
                """
                for i in self.browser.find_element_by_tag_name('p').text:
                    if i.isnumeric():
                        cards_val += str(i)

                """
                Create task
                """
                WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.ID, 'id_title'))
                ).send_keys(title_val)

                WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.ID, 'id_description'))
                ).send_keys(desc_val)

                WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.NAME, 'create_task'))
                ).click()

                message_create = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'alert'))
                )
                assert 'Задача успешно создана!' in message_create.text

                """
                Number of cards increased by 1
                """
                number_cards = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.TAG_NAME, 'p'))
                )
                assert "{} карточек".format(
                    int(cards_val) + 1
                ) in number_cards.text

                """
                The card was created?
                """
                card_text = self.browser.find_element_by_tag_name(
                    'div.item-row > div > span'
                )
                assert title_val in card_text.text

                """
                Update task
                """
                WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'edit'))
                ).click()

                """
                Message on edit page
                """
                message_edit = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'alert'))
                )
                assert 'Редактировать' in message_edit.text

                """
                Specified text on the card
                """
                original_id_title = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.ID, 'id_title'))
                )
                assert original_id_title.get_attribute('value') in title_val

                original_id_description = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.ID, 'id_description'))
                )
                assert original_id_description.text in desc_val

                """
                Passing text to the fields and update the task
                """
                self.browser.find_element_by_id('id_title').send_keys(' edit')
                self.browser.find_element_by_id(
                    'id_description'
                ).send_keys(' edit')

                WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.ID, 'id_complete'))
                ).click()

                WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.NAME, 'update_task'))
                ).click()

                """
                Pop-up message on the main page
                """
                message_update = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'alert'))
                )
                assert 'Задача успешно обновлена!' in message_update.text

                """
                Title and tag updated
                """
                card_update_text = self.browser.find_element_by_tag_name(
                    'div.item-row > div > strike'
                )
                assert title_val + ' edit' in card_update_text.text

                """
                Description updated
                """
                WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'edit'))
                ).click()
                assert desc_val + ' edit' in self.browser.find_element_by_id(
                    'id_description'
                ).text

                """
                The cancel button sent us to the main page
                """
                WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((
                        By.CLASS_NAME, 'cancel_button'
                    ))
                ).click()
                assert 'Создать' in self.browser.find_element_by_name(
                    'create_task'
                ).get_attribute('value')

                """
                Deleting task
                """
                WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'delete'))
                ).click()

                message_delete = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'alert'))
                )
                assert 'Удалить задачу' in message_delete.text

                """
                Check if the visible description and buttons, deleting the task
                """
                delete_text = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.TAG_NAME, 'p'))
                )
                assert delete_text

                cancel_delete = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((
                        By.CLASS_NAME, 'cancel_button'
                    ))
                )
                assert cancel_delete

                WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.NAME, 'confirm'))
                ).click()

                """
                Message on the main page after delete
                """
                message_success_delete = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, 'alert'))
                )
                assert 'Задача удалена!' in message_success_delete.text

                """
                Checking the number of cards
                """
                number_cards = WebDriverWait(self.browser, 10).until(
                    EC.visibility_of_element_located((By.TAG_NAME, 'p'))
                )
                assert "{} карточек".format(
                    int(cards_val)
                ) in number_cards.text

            finally:
                self.browser.quit()
