# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0004_auto_20160925_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='post_free_job',
            field=models.BooleanField(default=False),
        ),
    ]