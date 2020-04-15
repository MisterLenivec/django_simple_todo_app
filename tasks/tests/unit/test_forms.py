from django.test import TestCase

from tasks.forms import TaskForm


class TaskFormTests(TestCase):
    """
    Tests for task forms
    """
    def test_forms_task_input_task_has_placeholder(self):
        """
        Check that placeholder task exist
        """
        form = TaskForm()
        self.assertIn('placeholder="Задача"', form.as_p())

    def test_forms_task_input_description_has_placeholder(self):
        """
        Check that placeholder description exist
        """
        form = TaskForm()
        self.assertIn('placeholder="Описание"', form.as_p())

    def test_can_create_a_task_with_just_a_title(self):
        """
        Task creation with title only
        """
        form = TaskForm({'title': 'Create a test task'})
        self.assertTrue(form.is_valid())

    def test_can_create_a_task_with_just_a_description(self):
        """
        Task creation with description only, expected fail
        """
        form = TaskForm({'description': 'Create a test desription'})
        self.assertFalse(form.is_valid())

    def test_form_is_not_valid_for_missing_title(self):
        """
        Task creation without title, expected form is not valid
        """
        form = TaskForm({'title': ''})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_title(self):
        """
        Task creation without title, expected correct error message
        """
        form = TaskForm({'title': ''})
        self.assertEqual(form.errors['title'], ['Обязательное поле.'])

    def test_too_long_title_is_not_valid(self):
        """
        Form is not valid if string longer than 50 symbols
        """
        form = TaskForm({'title': 51 * 'Q'})
        self.assertFalse(form.is_valid())

    def test_correct_message_for_too_long_title(self):
        """
        Expected error message if string longer than 50 symbols
        """
        form = TaskForm({'title': 51 * 'Q'})
        self.assertEqual(
            form.errors,
            {'title': ['Убедитесь, что это значение содержит не более 50 '
                       'символов (сейчас 51).']}
        )
