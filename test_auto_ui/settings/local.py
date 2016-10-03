from .base import BASE_DIR
import os
import dj_database_url

DEBUG = True
db_env = dj_database_url.config()
db_env['TYPE'] = 'postgres' 
DATABASES= { 'default': db_env}


MEDIA_ROOT = '/app/test_auto_ui/media'
MEDIA_URL =  '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/app/test_auto_ui/static',
]
