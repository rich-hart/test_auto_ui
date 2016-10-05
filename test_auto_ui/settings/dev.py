from .base import *

ALLOWED_HOSTS = ['127.0.0.1']

MEDIA_ROOT = '/var/www/test_auto_ui/media'
MEDIA_URL = '/media/'

STATIC_ROOT = '/var/www/test_auto_ui/static'
STATIC_URL = '/static/'

DEBUG = True
try:
    from .local import *
except ImportError:
    pass
