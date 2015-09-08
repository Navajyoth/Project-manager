from django.conf.urls import patterns, url, include
from rest_framework_nested import routers

from .views import WorkTypeViewSet, TechnologyViewSet

router = routers.SimpleRouter()
router.register('worktypes', WorkTypeViewSet, base_name='worktypes')
router.register('technologies', TechnologyViewSet, base_name='technologies')

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
)
