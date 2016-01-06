FEEDBACK_EMAIL = 'developer@bunchcut.com'

ADMINS = (
    ('developer', 'developer@bunchcut.com'),
)
MANAGERS = ADMINS

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/app-messages'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'developer@bunchcut.com'
EMAIL_HOST_PASSWORD = 'LetsBuildAnAppinct'
EMAIL_PORT = 587


COMPRESS_ENABLED = False

URL_DOMAIN = "bunchcut.local"
URL_PREFIX = "http://" + URL_DOMAIN
SESSION_COOKIE_DOMAIN = '.' + URL_DOMAIN

INTERCOM_API_KEY = "8e972e35e79214cf15db952edafaee7584072c16"
INTERCOM = "31koswr2"

DISABLED_APPS = ['raven.contrib.django.raven_compat']
