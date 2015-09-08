from django.test import TestCase
from model_mommy import mommy

from apps.projects.models import Project, ProjectWork
from apps.utils.tests import console_log


class ProjectModelTest(TestCase):

    def setUp(self):
        self.item = mommy.make(Project)

    def test_project_model(self):
        self.assertTrue(isinstance(self.item, Project))
        console_log('core', 'model', 'Project')


class ProjectWorkModelTest(TestCase):

    def setUp(self):
        self.item = mommy.make(ProjectWork)

    def test_project_work_model(self):
        self.assertTrue(isinstance(self.item, ProjectWork))
        console_log('core', 'model', 'ProjectWork')
