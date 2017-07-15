# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Detail
from .models import Course

admin.site.register(Course)
admin.site.register(Detail)
# Register your models here.
