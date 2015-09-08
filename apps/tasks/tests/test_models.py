from django.test import TestCase

from model_mommy import mommy

from apps.tasks.models import Task, Commit
from apps.utils.tests import console_log


class TaskModelTest(TestCase):

    def setUp(self):
        self.item = mommy.make(Task)

    def test_task_model(self):
        self.assertTrue(isinstance(self.item, Task))
        console_log('tasks', 'model', 'Task')


class CommitModelTest(TestCase):

    def setUp(self):
        self.item = mommy.make(Commit)

    def test_commit_model(self):
        console_log('tasks', 'model', 'Commit')
