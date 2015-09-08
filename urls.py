from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib import admin

from apps.core.views import home_view


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.account.urls', namespace="account")),
    url(r'^', include('apps.projects.urls', namespace="projects")),
    url(r'^', include('apps.tasks.urls', namespace="tasks")),
    url(r'^', include('apps.core.urls', namespace="core")),
    url(r'^', include('apps.knowledge.urls', namespace="knowledge")),
    url(r'^google', include('apps.google.urls')),
    url(r'^thank-you/$', TemplateView.as_view(template_name="thankyou.html"), name="thankyou"),
    url(r'^/error/$', TemplateView.as_view(template_name="error.html"), name="error"),
    url(r'^$', home_view, name="home"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns(
    '',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}))
