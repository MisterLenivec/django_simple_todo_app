from django.core.exceptions import ValidationError
from django.test import TestCase

from tasks.models import Task


class TaskModelTests(TestCase):
    """
    Tests for task model
    """
    def test_default_text(self):
        """
        Empty task test
        """
        task = Task()
        self.assertEqual(task.title, '')

    def test_task_title_equal_expected_title(self):
        """
        If title not equal expected title, then False is returned.
        """
        task = Task(title='Test title')
        task.save()
        self.assertEqual(task.title, 'Test title')

    def test_complete_defaults_to_false(self):
        """
        If done not properly specified, then False is returned.
        """
        task = Task(title='Test title')
        task.save()
        self.assertFalse(task.complete)

    def test_can_create_a_task_with_a_title_and_status_complete(self):
        """
        If done not properly specified, then False is returned.
        """
        task = Task(title='Test title', complete=True)
        task.save()
        self.assertEqual(task.title, 'Test title')  # No need?
        self.assertTrue(task.complete)

    def test_string_representation(self):
        """
        Is the type of the object equal to string type?
        """
        task = Task(title="Test title")
        self.assertEqual('Test title', str(task))

    def test_task_as_a_string(self):
        """
        Test title given to object is equal to the task as a string
        """
        task = Task(title="Test title")
        self.assertEqual(type(task.title), type('Random string'))

    def test_too_long_task_title(self):
        """
        Fail if string longer than 50 symbols
        """
        with self.assertRaises(Exception):
            Task.objects.create(title=51 * 'Q')

    def test_task_ordering(self):
        """
        Elements Order Test
        """
        task1 = Task.objects.create(title='A1')
        task2 = Task.objects.create(title='B2')
        task3 = Task.objects.create(title='C3')
        self.assertEqual(Task.objects.all()[0], task3)
        self.assertEqual(Task.objects.all()[1], task2)
        self.assertEqual(Task.objects.all()[2], task1)
        # Task model Meta ordering = ('-updated',)

    def test_cannot_save_empty_task(self):
        """
        An exception is caught when trying to save an empty object
        """
        task = Task(title='')
        with self.assertRaises(ValidationError):
            task.save()
            task.full_clean()
