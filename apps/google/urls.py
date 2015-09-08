from django.conf.urls import patterns, url
from .views import login, callback

urlpatterns = patterns('',
    url(r'/login/', login, name="google_login"),
    url(r'/callback/', callback, name="google_callback"),

)