from __future__ import absolute_import

from celery import Celery
from django.conf import settings

CELERY_RESULT_BACKEND = 'db+{TYPE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(**settings.DATABASES['default'])

app = Celery('inspection',
             broker='django://',
             backend=CELERY_RESULT_BACKEND,
             include=['inspection.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
)

if __name__ == '__main__':
    app.start()

