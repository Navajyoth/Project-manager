from django.test import TestCase
from model_mommy import mommy

from apps.core.models import WorkType, Technology
from apps.utils.tests import console_log


class WorkTypeModelTest(TestCase):

    def setUp(self):
        self.item = mommy.make(WorkType)

    def test_model(self):
        self.assertTrue(isinstance(self.item, WorkType))
        console_log('core', 'model', 'WorkType')


class TechnologyModelTest(TestCase):

    def setUp(self):
        self.item = mommy.make(Technology)

    def test_model(self):
        self.assertTrue(isinstance(self.item, Technology))
        console_log('core', 'model', 'Technology')
