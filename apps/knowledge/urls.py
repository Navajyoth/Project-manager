from django.conf.urls import patterns, url, include
from rest_framework_nested import routers
from .views import QuoteViewSet, ArticleViewSet


router = routers.SimpleRouter()
router.register('quotes', QuoteViewSet, base_name='quotes')
router.register('articles', ArticleViewSet, base_name='articles')

urlpatterns = patterns(
    '',
    url(r'api/', include(router.urls)),
)
