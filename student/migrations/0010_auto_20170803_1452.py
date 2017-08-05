# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20170722_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('middle_name', models.CharField(max_length=150)),
                ('course', models.ManyToManyField(related_name='Profesor', to='student.Course')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='subject',
            field=models.ManyToManyField(related_name='Profesor', to='student.Subject'),
        ),
    ]
