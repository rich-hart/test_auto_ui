import os
import urlparse

DEBUG = False

url = urlparse.urlparse(os.environ["DATABASE_URL"])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
        'TYPE': 'postgres',
    }
}
