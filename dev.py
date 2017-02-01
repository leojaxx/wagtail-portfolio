from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# PostgreSQL (Recommended, but requires the psycopg2 library and Postgresql development headers)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',  # Set to empty string for localhost.
        'PORT': '',  # Set to empty string for default.
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
    }
}


try:
    from .local import *
except ImportError:
    pass
