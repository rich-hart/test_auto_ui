#!/bin/bash

NAME="test_auto_ui"                                  # Name of the application
DJANGODIR=/vagrant/src/test_auto_ui             # Django project directory
SOCKFILE=/var/www/test_auto_ui/run/gunicorn.sock  # we will communicte using this unix socket
USER=root                                     # the user to run as
GROUP=root                               # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=test_auto_ui.settings.dev            # which settings file should Django use
DJANGO_WSGI_MODULE=test_auto_ui.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /vagrant/src/test_auto_ui/venv/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /vagrant/src/test_auto_ui/venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=- \
#  --user=$USER --group=$GROUP 
