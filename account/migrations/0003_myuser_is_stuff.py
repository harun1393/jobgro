# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_myuser_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_stuff',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]