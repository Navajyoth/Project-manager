from rest_framework.test import force_authenticate, APITestCase
from model_mommy import mommy

from apps.knowledge.models import Quote, Article
from apps.account.models import User
from apps.utils.tests import BaseViewSetTestMixing


class QuoteViewSetTest(APITestCase, BaseViewSetTestMixing):
    url_name = "quotes"
    model = Quote
    app_name = "knowledge"

    def setUp(self):
        self.item = mommy.make(Quote)
        self.user = mommy.make(User)

        self.post_data = {
            "author": "Test Author",
            "text": "Test Quote1",
        }

        self.update_data = {
            "author": "Test Author",
            "text": "Test Quote2",
        }


class ArticleViewSetTest(APITestCase, BaseViewSetTestMixing):
    url_name = "articles"
    model = Article
    app_name = "knowledge"

    def setUp(self):
        self.item = mommy.make(Article)
        self.user = mommy.make(User)

        self.post_data = {
            "url": self.item.url,
            "title": "Test Article1",
        }

        self.update_data = {
            "url": self.item.url,
            "title": "Test Article2",
        }
