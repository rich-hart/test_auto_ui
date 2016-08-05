
## Install
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

## API Usage

Upload pdfs to /api/pdfs/
Create new options at /api/options/
Create computer vision tests at /api/cvtests/

To modify or delete pdfs, options, or tests locate the specify id of the object and add it to the end of the url like so: /api/{object}/{id} e.g. /api/cvtests/27. 
