from django.conf.urls import patterns, url, include
from rest_framework_nested import routers

from .views import ProjectViewSet, ProjectWorkViewSet


router = routers.SimpleRouter()
router.register('projects', ProjectViewSet, base_name='projects')
router.register('ProjectWorks', ProjectWorkViewSet, base_name='ProjectWorks')

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
)
