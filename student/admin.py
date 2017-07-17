# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


class StudentAdmin(admin.ModelAdmin):
    fieldset = [
	    ("Student Details", {"field":["first_name","last_name"]})
	]
	
	def student_course(self, obj);
	    return obj.list_course()
		
list_display = ("first_name","last_name",)
		
from .models import Detail
from .models import Course



# Register your models here.
