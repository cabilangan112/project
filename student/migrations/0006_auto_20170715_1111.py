# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 03:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20170715_1111'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
    ]
