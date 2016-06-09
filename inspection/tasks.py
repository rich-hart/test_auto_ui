from __future__ import absolute_import
import subprocess
from inspection.celery import app

import urllib.request

from .models import CVTest

import subprocess

@app.task
def inspect(test_id):
    cvtest = CVTest.objects.filter(id=test_id)[0]
    pdf_a_path = cvtest.pdf_a.pdf_file.path
    pdf_b_path = cvtest.pdf_b.pdf_file.path
    options = cvtest.options.option_string
    command = "ox_inspect {0}".format(options)
    cvtest.results = subprocess.check_output(command.split())
    cvtest.save() 
    
