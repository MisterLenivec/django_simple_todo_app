from django.test import TestCase
from django.shortcuts import get_object_or_404

from tasks.models import Task
from tasks.forms import TaskForm


class ViewsTests(TestCase):
    """
    Tests for task views
    """
    # def setUp(self) -> None:
    #     self.page = self.client.get("/")
    #     self.task = Task.objects.create(title='test title',
    #                                     description='test description',
    #                                     complete=True)
    #
    # def tearDown(self) -> None:
    #     self.task.delete()

    def test_get_base_page(self):
        """
        Check index page status code and used template
        """
        self.page = self.client.get("/")
        self.assertEqual(self.page.status_code, 200)
        self.assertTemplateUsed(self.page, "base.html")

    def test_get_list_page(self):
        """
        Check index page status code, used template and form
        """
        self.page = self.client.get("/")
        self.assertEqual(self.page.status_code, 200)
        self.assertTemplateUsed(self.page, 'tasks/list.html')
        self.assertIsInstance(self.page.context['form'], TaskForm)

    def test_get_update_page(self):
        """
        Check update page status code, used template and form
        """
        self.task = Task.objects.create(title='test title',
                                        description='test description',
                                        complete=True)
        self.page = self.client.get('/update_task/{}/'.format(self.task.id))
        self.assertEqual(self.page.status_code, 200)
        self.assertTemplateUsed(self.page, 'tasks/update_task.html')
        self.assertIsInstance(self.page.context['form'], TaskForm)

    def test_get_delete_page(self):
        """
        Check delete page status code, used template and form
        """
        self.task = Task.objects.create(title='test title',
                                        description='test description',
                                        complete=True)
        self.page = self.client.get('/delete_task/{}/'.format(self.task.id))
        self.assertEqual(self.page.status_code, 200)
        self.assertTemplateUsed(self.page, 'tasks/delete_task.html')

    def test_get_update_page_for_task_does_not_exist(self):
        """
        Try update with invalid data test
        """
        with self.assertRaises(Exception):
            self.page = self.client.get('/update_task/1/')
            self.assertRaises(self.page.status_code, 200)

    def test_post_create_a_task(self):
        """
        Create 2 tasks with post data
        """
        self.client.post('', data={'title': 'Test task'})
        self.assertEqual(Task.objects.count(), 1)
        task = Task.objects.first()
        self.assertEqual(task.title, 'Test task')
        self.assertEqual(task.description, '')
        self.assertEqual(task.complete,  False)

        self.client.post('', data={'title': 'Second test task',
                                   'description': 'Some test description',
                                   'complete': True})
        self.assertEqual(Task.objects.count(), 2)
        task = Task.objects.all()[0]
        # Not [1] because Task model Meta ordering = ('-updated',)
        self.assertEqual(task.title, 'Second test task')
        self.assertEqual(task.description, 'Some test description')
        self.assertEqual(task.complete, True)

    def test_post_create_a_task_with_empty_input(self):
        """
        Create a task with empty input
        """
        self.client.post('', data={'title': ''})
        self.assertEqual(Task.objects.count(), 0)

    def test_post_update_a_task(self):
        """
        Update task with post data
        """
        task = Task.objects.create(title='test title',
                                   description='test description',
                                   complete=False)
        task.save()
        self.client.post("/update_task/{}/".format(task.id),
                         data={'title': 'Another title',
                               'description': 'Another test descr',
                               'complete': True})
        update_task = get_object_or_404(Task, pk=task.id)
        # update_task = Task.objects.get(pk=task.id)
        # update_task = Task.objects.first()
        self.assertEqual('Another title', update_task.title)
        self.assertEqual('Another test descr', update_task.description)
        self.assertEqual(True, update_task.complete)

    def test_complete_toggle_status(self):
        """
        Test for switch check - complete
        """
        task = Task(title="A test title")
        task.save()
        task = get_object_or_404(Task, pk=task.id)
        self.assertEqual(task.complete, False)
        task.complete = True
        self.assertEqual(task.complete, True)
