"""form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from student.views import list_student,Professorlist,Courselist,Subjectlist,facultylist,facultys_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$',list_student, name='student'),
	url(r'^courses/$',Courselist.as_view(), name='Course'),
	url(r'^subjects/$',Subjectlist.as_view(), name='Subject'),
	url(r'^professors/$',Professorlist.as_view(), name='Professor'),	
	url(r'^facultys/$',facultylist.as_view(), name='faculty'),
#	url(r'^$',facultys_list, name='faculty'),
]
