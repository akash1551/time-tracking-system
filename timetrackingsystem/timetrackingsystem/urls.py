"""timetrackingsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^update/team/', add_team),
    url(r'^update/employee/$', add_employee),
    url(r'^add/shift/$', add_shift),
    url(r'^edit/employee/$', edit_employee),
    url(r'^start/break/$',start_break),
    url(r'^end/break/$',end_break),
    url(r'^calculate/working_time$', calculate_working_hours),
    url(r'^registration/$',  registration_page),
    url(r'^adding/shift/$',  shifttime_page),
    url(r'^edit/employee/page/$',  edit_employee_page),
    url(r'^started/Break/$', breaktime_page),
    url(r'^end/Break/page/$', end_break_page),
    url(r'^working/hours/page/$', working_hours_page),
    url(r'^add/team/$',team_add_page),
    url(r'^show/employee/$',show_employee),


]
