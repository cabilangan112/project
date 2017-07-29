# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

from .models import Detail
from .models import Course
from .models import Subject
# Create your views here.
def list_student(request):
	student = Detail.objects.exclude()
	context = {
	'student' :student,
	}
	return render(request,"index.html",context)

class Courselist(View):
	def get(self,request):
		courses = Course.objects.all()
		context = {
		'courses' :courses,
		}
		return render(request,"course.html",context)

class Subjectlist(View):
	def get(self,request):
		subjects = Subject.objects.all()
		context = {
		'subjects' :subjects,
		}
		return render(request,"subject.html",context)