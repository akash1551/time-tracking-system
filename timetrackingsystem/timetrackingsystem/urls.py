from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^update/team/',add_team),
    url(r'^update/employee/$',add_employee),
    url(r'^add/shift/$',add_shift),
    url(r'^edit/employee/$',edit_employee),
    url(r'^start/break/$',start_break),
    url(r'^end/break/$',end_break),
    url(r'^calculate/working_time/$',calculate_working_hours),
    url(r'^registration/$',registration_page),
    url(r'^adding/shift/$',shifttime_page),
    url(r'^edit/employee/page/$',edit_employee_page),
    url(r'^started/Break/$',breaktime_page),
    url(r'^end/Break/page/$',end_break_page),
    url(r'^working/hours/page/$',working_hours_page),
    url(r'^add/team/$',team_add_page),
    url(r'^show/employee/$',show_employee),
    url(r'^login/$',login),
    url(r'^login/page/$',login_page),
    url(r'^timetrackingsystem/page/$',timetrackingsystem_page),
]
