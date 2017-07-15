# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Details(models.Model):
	first_name =  models.CharField(max_length=150)
	last_name =  models.CharField(max_length=150)
	MI =  models.CharField(max_length=150)
	age =  models.IntegerField()
	birthday = models.DateTimeField()
	Course = models.CharField(max_length=100)
	