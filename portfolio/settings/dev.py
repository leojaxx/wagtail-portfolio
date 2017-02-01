from __future__ import absolute_import, unicode_literals
from .base import *


DEBUG = True

SECRET_KEY = 'no(40m2fqaes(v1pouf#6dfx$wk-^gjkhu7m*6%zt7+oec67tg'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'portfoliodb',
        'USER': 'leo',
        'PASSWORD': 'ipostdj',
        'HOST': '127.0.0.1',
        'PORT': '',
        'CONN_MAX_AGE': 600,
    }
}

try:
    from .local import *
except ImportError:
    pass
