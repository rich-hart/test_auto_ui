# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-11 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0003_auto_20160707_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='pdf_file',
            field=models.FileField(upload_to='/Users/openstax/workspace/test_auto_ui/media/pdf'),
        ),
    ]
