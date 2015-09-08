from .base import *
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {}
DATABASES['default'] = dj_database_url.config()

GMAIL_CLIENT_ID = '585377997899-5tmrkspc8t0i2igbibpd1g582buq2tfl.apps.googleusercontent.com'
GMAIL_CLIENT_SECRET = 'A1jN7kTOlp0UoRI49SW674Hl'
GMAIL_SCOPE = 'https://www.googleapis.com/auth/plus.me email'
GMAIL_REDIRECT_URI = 'http://proman-django.herokuapp.com/google/callback'

BASE_URL = "http://proman-django.herokuapp.com/"
