from rest_framework.test import force_authenticate, APITestCase
from model_mommy import mommy

from apps.utils.tests import console_log, BaseViewSetTestMixing
from apps.core.models import WorkType, Technology
from apps.account.models import User


class WorkTypeViewSetTest(APITestCase, BaseViewSetTestMixing):
    url_name = "worktypes"
    model = WorkType
    app_name = "core"

    def setUp(self):
        self.user = mommy.make(User)
        self.item = mommy.make(WorkType)
        self.post_data = {
            'name': 'test work type1',
        }
        self.update_data = {
            'name': 'test work type2',
        }


class TechnologyViewSetTest(APITestCase, BaseViewSetTestMixing):
    url_name = "technologies"
    model = Technology
    app_name = "core"

    def setUp(self):
        self.user = mommy.make(User)
        self.item = mommy.make(Technology)
        self.post_data = {
            'name': 'test technology 1',
            'is_deleted': False
        }
        self.update_data = {
            'name': 'test technology 1',
            'is_deleted': True
        }
