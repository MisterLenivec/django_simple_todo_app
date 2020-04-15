from django.apps import apps
from django.test import TestCase

from tasks.apps import TasksConfig


class TasksConfigTests(TestCase):
    """
    App config name test
    """
    def test_apps(self):
        """
        App config name is tasks
        """
        self.assertEqual('tasks', TasksConfig.name)
        self.assertEqual('tasks', apps.get_app_config('tasks').name)
