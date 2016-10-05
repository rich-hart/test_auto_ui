from .base import *

ALLOWED_HOSTS = ['127.0.0.1','.cnx.org']

try:
    from .local import *
except ImportError:
    pass
