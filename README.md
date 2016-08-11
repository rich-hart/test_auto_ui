## Requirements
Ubuntu >= 14.10
Postgresql >= 9.3
Python >= 3.5

## Install & Run

First install inspection dependencies at https://github.com/openstax/test-automation/tree/master/inspection, then install the webserver:

``` .sh
git clone https://github.com/rich-hart/test_auto_ui.git
cd test_auto_ui
virtualenv -p $(which python3.5) venv
source venv/bin/activate
pip install -U pip
pip install -r requirements/dev.txt
createdb -U postgres qa_automation
./manage.py migrate
./manage.py loaddata fixture.yaml 
./manage.py createsuperuser
./manage.py runserver
```

In another terminal got to the test_auto_ui directory and start the worker queue:
```
export DJANGO_SETTINGS_MODULE=test_auto_ui.settings
celery -A inspection worker -l info
```

## API Usage

Upload pdfs to ``/api/pdfs/``

Create new options at ``/api/options/``

Create computer vision tests at ``/api/cvtests/``

To modify or delete pdfs, options, or tests locate the specify id of the object and add it to the end of the url like so: ``/api/{object}/{id}`` e.g. ``/api/cvtests/27``. 

## Notes

The tool works best on pdfs that have had minor to moderate alterations to them.  Tests on PDFs that are around several hundred pages long can take a few hours to run.  PDFs over 1000 pages should be run over night.

Computer vision tests are run by a worker queue so several tests can initiated at the same time.  

This is the program the django server is running to perform the cv tests https://github.com/openstax/test-automation/tree/master/inspection. 
