# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 04:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20160924_0436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='is_stuff',
            new_name='is_staff',
        ),
    ]