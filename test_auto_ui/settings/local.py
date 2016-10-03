import os
import dj_database_url

DEBUG = True
db_env = dj_database_url.config()
db_env['TYPE'] = 'postgres' 
DATABASES= { 'default': db_env}


MEDIA_ROOT = STATIC_ROOT
MEDIA_URL =  STATIC_URL 

