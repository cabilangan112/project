# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Detail
from .models import Course


class StudentAdmin(admin.ModelAdmin):
    fieldset = [
	    ("Student Detail", {"field":["first_name","last_name"]})
	]
	
def student_Course(self, obj):
	return obj.list_Course()
		
list_display = ("first_name","last_name",)

admin.site.register(Detail)
admin.site.register(Course)


# Register your models here.
