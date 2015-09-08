import json

from rest_framework.test import force_authenticate, APITestCase
from model_mommy import mommy

from apps.utils.tests import console_log, BaseViewSetTestMixing
from apps.projects.models import Project, ProjectWork
from apps.core.models import WorkType
from apps.tasks.models import Task, Commit
from apps.account.models import User


class TaskViewSetTest(APITestCase, BaseViewSetTestMixing):
    url_name = "tasks"
    model = Task
    app_name = "tasks"

    def setUp(self):
        """
        only limited fields are chosen.
        """
        self.user = mommy.make(User)
        self.user1 = mommy.make(User)
        self.project = mommy.make(Project)
        self.item = mommy.make(Task, project=self.project)
        self.item1 = mommy.make(Task, project=self.project, user=self.user)
        self.item2 = mommy.make(Task, project=self.project, user=self.user)
        self.item3 = mommy.make(Task, project=self.project, user=self.user1)
        self.post_data = {
            "title": "Test Task",
            "description": "Test Task1",
            "user": self.user.id,
            "status": "backlog",
            "project": self.project.id
        }

        self.update_data = {
            "title": "Test Task",
            "description": "Test Task2",
            "user": self.user.id,
            "status": "backlog",
            "project": self.project.id
        }

    def test_list_route(self):
        """
        Testing list route to list current user's tasks.
        """
        url = '/api/tasks/user/'
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format='json')
        response.render()
        response_dict = json.loads(response.content)
        id_list = [item['id'] for item in response_dict]

        self.assertEqual(response.status_code, 200)
        self.assertIn(self.item1.id, id_list)
        self.assertIn(self.item2.id, id_list)
        self.assertNotIn(self.item3.id, id_list)
        console_log(self.app_name, 'GET', url, "Get current user's items")


class CommitViewSetTest(APITestCase, BaseViewSetTestMixing):
    url_name = "commits"
    model = Task
    app_name = "tasks"

    def setUp(self):
        self.user = mommy.make(User)
        self.task = mommy.make(Task)
        self.item = mommy.make(Commit, task=self.task)

        self.post_data = {
            'task': self.task.id,
            'url': "http://127.0.0.1:8000/"
        }

        self.update_data = {
            'task': self.task.id,
            'url': "http://127.0.0.1:8000/admin"
        }
