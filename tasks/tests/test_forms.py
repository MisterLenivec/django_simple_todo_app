from django.test import TestCase

from tasks.forms import TaskForm


class TaskFormTests(TestCase):
    """
    Tests for task forms
    """
    def test_forms_task_inputs_has_placeholder(self):
        """
        Check that placeholder tasks exist
        """
        form = TaskForm()
        self.assertIn('placeholder="Задача"', form.as_p())
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

    def test_correct_message_for_missing_title(self):
        """
        Task creation without title, expected fail
        """
        form = TaskForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['Обязательное поле.'])

    def test_too_long_title(self):
        """
        Fail if string longer than 50 symbols
        """
        form = TaskForm({'title': 51 * 'Q'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors,
            {'title': ['Убедитесь, что это значение содержит не более 50 символов (сейчас 51).']}
        )
