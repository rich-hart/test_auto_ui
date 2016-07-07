from __future__ import absolute_import
import subprocess
from inspection.celery import app

import urllib.request

from .models import CVTest

import subprocess

import tempfile

import shutil

from os.path import join

import ntpath

import pwd
import grp
import os
from datetime import datetime

from django.conf import settings
@app.task
def inspect(test_id):
    cvtest = CVTest.objects.filter(id=test_id)[0]
    pdf_a_path = cvtest.pdf_a.pdf_file.path
    pdf_b_path = cvtest.pdf_b.pdf_file.path
    options = cvtest.options.option_string
    command = "ox_inspect {0}".format(options)
    cvtest.started = datetime.now()
    cvtest.save()
    with tempfile.TemporaryDirectory() as tmpdirname:
        
        pdf_a_filename = ntpath.basename(pdf_a_path)
        temp_pdf_a_path = join(tmpdirname,pdf_a_filename)
        shutil.copy2(pdf_a_path,tmpdirname)

        pdf_b_filename = ntpath.basename(pdf_b_path)
        temp_pdf_b_path = join(tmpdirname,pdf_b_filename)
        shutil.copy2(pdf_b_path,temp_pdf_b_path)


        command = "ox_inspect {0} {1} {2}".format(options or '',
                                                  temp_pdf_a_path, 
                                                  temp_pdf_b_path)

        cvtest.results = subprocess.check_output(command.split())
    cvtest.finished = datetime.now()
    cvtest.save() 
    return cvtest.results
    
