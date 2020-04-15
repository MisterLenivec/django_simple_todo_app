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

    def test_get_base_page_status_code(self):
        """
        Check index page status code
        """
        self.page = self.client.get("/")
        self.assertEqual(self.page.status_code, 200)

    def test_page_is_base_page(self):
        """
        Check index page template correct
        """
        self.page = self.client.get("/")
        self.assertTemplateUsed(self.page, "base.html")

    def test_page_is_list_page(self):
        """
        Check list page template is correct
        """
        self.page = self.client.get("/")
        self.assertTemplateUsed(self.page, 'tasks/list.html')

    def test_list_page_use_correct_form(self):
        """
        Check list page use correct form
        """
        self.page = self.client.get("/")
        self.assertIsInstance(self.page.context['form'], TaskForm)

    def test_get_update_page_status_code(self):
        """
        Check update page status code
        """
        self.task = Task.objects.create(title='test title',
                                        description='test description',
                                        complete=True)
        self.page = self.client.get('/update_task/{}/'.format(self.task.id))
        self.assertEqual(self.page.status_code, 200)

    def test_update_page_template_is_correct(self):
        """
        Check update page template is correct
        """
        self.task = Task.objects.create(title='test title',
                                        description='test description',
                                        complete=True)
        self.page = self.client.get('/update_task/{}/'.format(self.task.id))
        self.assertTemplateUsed(self.page, 'tasks/update_task.html')

    def test_update_page_use_correct_form(self):
        """
        Check update page use correct form
        """
        self.task = Task.objects.create(title='test title',
                                        description='test description',
                                        complete=True)
        self.page = self.client.get('/update_task/{}/'.format(self.task.id))
        self.assertIsInstance(self.page.context['form'], TaskForm)

    def test_get_delete_page_status_code(self):
        """
        Check delete page status code
        """
        self.task = Task.objects.create(title='test title',
                                        description='test description',
                                        complete=True)
        self.page = self.client.get('/delete_task/{}/'.format(self.task.id))
        self.assertEqual(self.page.status_code, 200)

    def test_delete_page_use_correct_template(self):
        """
        Check delete page use correct template
        """
        self.task = Task.objects.create(title='test title',
                                        description='test description',
                                        complete=True)
        self.page = self.client.get('/delete_task/{}/'.format(self.task.id))
        self.assertTemplateUsed(self.page, 'tasks/delete_task.html')

    def test_get_update_page_for_task_does_not_exist(self):
        """
        Try update with invalid data test
        """
        with self.assertRaises(Exception):
            self.page = self.client.get('/update_task/1/')
            self.assertRaises(self.page.status_code, 200)

    def test_first_object_is_our_create_object(self):
        """
        Create tasks with post data without description
        """
        self.client.post('', data={'title': 'Should be 1 object'})
        task = Task.objects.first()
        self.assertEqual(task.title, 'Should be 1 object')

    def test_post_create_a_task_with_no_description(self):
        """
        Create tasks with post data without description
        """
        self.client.post('', data={'title': 'Test task'})
        task = Task.objects.first()
        self.assertEqual(task.description, '')

    def test_create_and_count_task(self):
        """
        Create task with post data and count
        """
        self.client.post('', data={'title': 'Test task'})
        self.assertEqual(Task.objects.count(), 1)

    def test_post_create_a_two_tasks_and_count_it(self):
        """
        Create 2 tasks with post data and count it
        """
        self.client.post('', data={'title': 'Test task'})
        self.client.post('', data={'title': 'Second test task',
                                   'description': 'Some test description',
                                   'complete': True})
        self.assertEqual(Task.objects.count(), 2)

    def test_order_objects_created(self):
        """
        Create 2 tasks with post data and check order of objects
        """
        self.client.post('', data={'title': 'Test task'})
        self.client.post('', data={'title': 'Second test task',
                                   'description': 'Some test description',
                                   'complete': True})
        task = Task.objects.all()[0]
        # Not [1] because Task model Meta ordering = ('-updated',)
        self.assertEqual(task.title, 'Second test task')

    def test_post_create_a_task_with_empty_input(self):
        """
        Create a task with empty input
        """
        self.client.post('', data={'title': ''})
        self.assertEqual(Task.objects.count(), 0)

    def test_post_update_check_task_title(self):
        """
        Update task with post data, check title
        """
        task = Task.objects.create(title='test title',
                                   description='test description',
                                   complete=False)
        task.save()
        self.client.post("/update_task/{}/".format(task.id),
                         data={'title': 'Another title for check title',
                               'description': 'Another descr for check title',
                               'complete': True})
        update_task = get_object_or_404(Task, pk=task.id)
        # update_task = Task.objects.get(pk=task.id)
        # update_task = Task.objects.first()
        self.assertEqual('Another title for check title', update_task.title)

    def test_post_update_check_task_description(self):
        """
        Update task with post data, check description
        """
        task = Task.objects.create(title='test title',
                                   description='test description',
                                   complete=False)
        task.save()
        self.client.post("/update_task/{}/".format(task.id),
                         data={'title': 'Another title for check descr',
                               'description': 'Descr for check descr',
                               'complete': True})
        update_task = get_object_or_404(Task, pk=task.id)
        self.assertEqual('Descr for check descr', update_task.description)

    def test_post_update_check_task_complete(self):
        """
        Update task with post data, check complete
        """
        task = Task.objects.create(title='test title',
                                   description='test description',
                                   complete=False)
        task.save()
        self.client.post("/update_task/{}/".format(task.id),
                         data={'title': 'Another title for check complete',
                               'description': 'Descr for check complete',
                               'complete': True})
        update_task = get_object_or_404(Task, pk=task.id)
        self.assertEqual(True, update_task.complete)

    def test_complete_toggle_status_to_true(self):
        """
        Test for switch check - complete must be true
        """
        task = Task(title="A test title", complete=False)
        task.save()
        task = get_object_or_404(Task, pk=task.id)
        task.complete = True
        self.assertEqual(task.complete, True)

    def test_complete_toggle_status_to_false(self):
        """
        Test for switch check - complete must be false
        """
        task = Task(title="A test title", complete=True)
        task.save()
        task = get_object_or_404(Task, pk=task.id)
        task.complete = False
        self.assertEqual(task.complete, False)
