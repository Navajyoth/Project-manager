from rest_framework_nested import routers
from django.conf.urls import patterns, url, include
from . import views

router = routers.SimpleRouter()
router.register('users', views.UserViewSet, base_name='users')
router.register('user-technologies', views.UserTechnologyViewSet, base_name='user-technologies')

urlpatterns = patterns(
    '',
    url(r'^api/', include(router.urls)),
    url(r'^api-auth-token/$', views.ObtainAuthToken.as_view()),
    url(r'^profile/register/$', views.RegisterView.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^password/reset/(?P<id>[0-9]*)/(?P<key>[-\w\d]+)$', views.PasswordResetView.as_view(),
        name='password_reset'),
    url(r'^password/send-reset/$', views.SendPasswordResetMailView.as_view(), name='send_password_reset'),
    url(r'^email/send-verify/$', views.SendConfirmEmailView.as_view(), name='resend_email_confirm'),
    url(r'^email/confirm/(?P<id>[0-9]*)/(?P<key>[-\w\d]+)$', views.email_confirm_view, name='email_confirm'),
)
