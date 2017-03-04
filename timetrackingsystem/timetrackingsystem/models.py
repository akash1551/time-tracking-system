from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Employee(models.Model):
    user=models.OneToOneField(User,null=True)

    name=models.CharField(max_length=10)
    email=models.TextField()
    mobile_no=models.CharField(max_length=10,null=True)
    address=models.TextField(max_length=30,null=True)
    position=models.CharField(max_length=20)
    team_name = models.ForeignKey('Team')
    company = models.ForeignKey('Company')

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

class Company(models.Model):
    company = models.CharField(max_length=30)


    def __unicode__(self):
        return str(self.company)


class AttendanceSheet(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(Employee)
    ShiftTime = models.ForeignKey(ShiftTime)
    working_hours_time=models.DurationField(blank=True,null=True)

    def __unicode__(self):
        return str(self.date)


class Break(models.Model):
    start_break = models.DateTimeField(blank=True, null=True)
    end_break = models.DateTimeField(blank=True, null=True)
    attendance = models.ForeignKey(AttendanceSheet)


    def __str__(self):
        return str(self.attendance)



