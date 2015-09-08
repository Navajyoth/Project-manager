from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'proman',
        'USER': 'proman_user',
        'PASSWORD': 'abcd1234',
        'OPTIONS': {
            # "autocommit": True,
        },
    }
}

GMAIL_CLIENT_ID = '585377997899-5tmrkspc8t0i2igbibpd1g582buq2tfl.apps.googleusercontent.com'
GMAIL_CLIENT_SECRET = 'A1jN7kTOlp0UoRI49SW674Hl'
GMAIL_SCOPE = 'https://www.googleapis.com/auth/plus.me email'
GMAIL_REDIRECT_URI = 'http://127.0.0.1:8000/google/callback'


BASE_URL = "http://localhost:8000/"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': '_temp/logs/app.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'WARNING',
        },
        '_main': {
            'handlers': ['file'],
            'level': 'WARNING',
        },
    }
}
