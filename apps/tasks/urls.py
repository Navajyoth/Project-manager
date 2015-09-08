from django.conf.urls import patterns, url, include
from rest_framework_nested import routers

from .views import TaskViewSet, CommitViewSet, StatusLogViewSet

router = routers.SimpleRouter()
router.register('tasks', TaskViewSet, base_name='tasks')
router.register('commits', CommitViewSet, base_name='commits')
router.register('status-logs', StatusLogViewSet, base_name='status-logs')

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
)
