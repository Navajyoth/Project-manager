from rest_framework.test import force_authenticate, APITestCase
from model_mommy import mommy

from apps.utils.tests import console_log, BaseViewSetTestMixing
from apps.projects.models import Project, ProjectWork
from apps.core.models import WorkType
from apps.account.models import User


class ProjectsViewSetTest(APITestCase, BaseViewSetTestMixing):
    url_name = "projects"
    model = Project
    app_name = "projects"

    def setUp(self):
        self.user = mommy.make(User)
        self.item = mommy.make(Project)
        self.post_data = {
            'name': 'test work type1',
        }
        self.update_data = {
            'name': 'test work type2',
        }


class ProjectWorkViewSetTest(APITestCase, BaseViewSetTestMixing):
    url_name = "ProjectWorks"
    model = ProjectWork
    app_name = "projects"

    def setUp(self):
        self.user = mommy.make(User)
        self.work_type = mommy.make(WorkType)
        self.item = mommy.make(ProjectWork, work_type=self.work_type)
        self.post_data = {
            'work_type': self.work_type.id,
            'count': 10,
            'rate': 8.5
        }
        self.update_data = {
            'work_type': self.work_type.id,
            'count': 10,
            'rate': 9.5
        }
