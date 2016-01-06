from settings import *

ROOT_URLCONF = 'bunchcut.dev_urls'
FEEDBACK_EMAIL = 'dev_email_address@bunchcut.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bunchcut',
        'USER': 'bunchcut_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


TIME_ZONE = 'Africa/Johannesburg'

ADMINS = (
    ('developer', 'dev_email_address@bunchcut.com'),
)
MANAGERS = ADMINS


DEBUG = True
TEMPLATE_DEBUG = True
THUMBNAIL_DEBUG = DEBUG


ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FILE_PATH = '/tmp/app-messages'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'developer@bunchcut.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587



INTERCOM = "31koswr2"
INTERCOM_API_KEY = "8e972e35e79214cf15db952edafaee7584072c16"

COMPRESS_ENABLED = False

URL_DOMAIN = "bunchcut.local"
URL_PREFIX = "http://" + URL_DOMAIN
SESSION_COOKIE_DOMAIN = '.' + URL_DOMAIN

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, "bunchcut" ,"media_dev")
MEDIA_URL = "/media/"

DISABLED_APPS = ['raven.contrib.django.raven_compat']

ACTIVITY_EMAIL_DELAY_SECONDS = 2*60

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

