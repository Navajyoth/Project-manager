from django.test import TestCase

from model_mommy import mommy

from apps.knowledge.models import Quote, Article
from apps.utils.tests import console_log


class QuoteModelTest(TestCase):

    def setUp(self):
        self.item = mommy.make(Quote)

    def test_quote_model(self):
        self.assertTrue(isinstance(self.item, Quote))
        console_log('knowledge', 'model', 'Quote')


class ArticleModelTest(TestCase):

    def setUp(self):
        self.item = mommy.make(Article)

    def test_quote_model(self):
        self.assertTrue(isinstance(self.item, Article))
        console_log('knowledge', 'model', 'Article')
