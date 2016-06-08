from __future__ import absolute_import
import subprocess
from inspection.celery import app

import urllib.request

@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)

@app.task
def inspect(pdf_a_url, pdf_b_url, options):
    return "Not implemented"    
    
