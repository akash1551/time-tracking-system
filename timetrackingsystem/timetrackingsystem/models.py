from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Employee(models.Model):
    user=models.OneToOneField(User,null=True)
    
    name=models.CharField(max_length=10)
    email=models.TextField()
    mobile_no=models.CharField(max_length=10)
    address=models.TextField(max_length=30)
    position=models.CharField(max_length=20)
    team_name = models.ForeignKey('Team')

    def __unicode__(self):
        return str(self.name)


class ShiftTime(models.Model):
    start_shift_time=models.DateTimeField(blank=True, null=True)
    end_shift_time=models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return (str(self.start_shift_time) + ' ' + str(self.end_shift_time))


class Team(models.Model):
    team_name = models.CharField(max_length=30)
    

    def __unicode__(self):
        return str(self.team_name)


class AttendanceSheet(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(Employee)
    ShiftTime = models.ForeignKey(ShiftTime)


    def __unicode__(self):
        return str(self.date)


class Break(models.Model):
    BREAK_TYPE = (
                    (1,'start_break'),
                    (2,'end_break')
                 )
    attendance = models.ForeignKey(AttendanceSheet)
    break_time = models.DateTimeField(blank=True, null=True)
    break_type = models.IntegerField(choices=BREAK_TYPE)

    def __str__(self):
        return str(self.attendance)



