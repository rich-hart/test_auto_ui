
#### Install
``` .sh
git clone https://github.com/rich-hart/test_auto_ui.git
cd openstax-cms
pip install -r requirements/dev.txt
createdb -U postgres qa_automation
./manage.py migrate
./manage.py createsuperuser
export DJANGO_SETTINGS_MODULE=test_auto_ui.settings
celery -A inspection worker -l info
./manage.py runserver
```
