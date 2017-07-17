# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Detail(models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	middle_name = models.CharField(max_length=150)
	age = models.IntegerField()
	b_day = models.DateTimeField()
	course = models.ManytoManyField("Course",related_name="Detail")
	
	def __str__(self):
		return "{} by {}".format(self.first_name,self.list_course())

	def list_course(self):
		return ",".join([course.course_name for course in self.course.all()])

	def save(self, *args,**kwargs):
		super(Details,self).save(*args,**kwargs)

class Course(models.Model):
	course_name = models.CharField(max_length=150)
	course_description = models.TextField(max_length=550)
	
	def __str__(self):
		return self.course_name
