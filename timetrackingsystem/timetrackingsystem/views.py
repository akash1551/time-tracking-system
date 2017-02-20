import json,datetime
from datetime import timedelta
from .models import *
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
import dateutil.relativedelta 


def add_employee(request):
    jsonobj = json.loads(request.body)

    address = jsonobj.get('address')
    email = jsonobj.get('email')
    mobile_no= jsonobj.get('mobile_no')
    name =jsonobj.get('name')
    password = jsonobj.get('password')
    team_id = jsonobj.get('team_id')
    position = jsonobj.get('position')
    team_name = jsonobj.get('team_name')
    user=jsonobj.get('user')

    if name == None:
        return HttpResponse(json.dumps({"validation":"name should not be blank","status":False}), content_type="application/json")

    if((len(mobile_no) < 10) or (len(mobile_no) >10)):
        return HttpResponse(json.dumps({'validation':'invalid number', "status":False}), content_type="application/json")


    if len(password) < 8:
        return HttpResponse(json.dumps({'validation':'please enter minimum 8 characters', "status":False}), content_type="application/json")

    team = Team.objects.get(id=team_id)
    team.save()

    
    user = User.objects.create(username=user)
    user.set_password(password)
    user.save()
   
    employee = Employee.objects.create(user=user,name=name,email=email,mobile_no=mobile_no,position=position,address=address,team_name=team)
    employee.save()

    return HttpResponse(json.dumps({"validation":"employee added succesfully","status":True}), content_type="application/json")
   
def add_team(request):
    jsonobj = json.loads(request.body)

    team_name = jsonobj.get('team_name')

    if team_name == None:
        return HttpResponse(json.dumps({'validation':'please enter team name', "status":False}), content_type="application/json")


    team=Team.objects.create(team_name=team_name)
    team.save()

    return HttpResponse(json.dumps({'validation':'team name updated successfully', "status": True}), content_type="application/json")



def add_shift(request):
    jsonobj = json.loads(request.body)
    print jsonobj

    start_shift_time = jsonobj.get('start_shift_time')
    end_shift_time = jsonobj.get('end_shift_time')
    date = jsonobj.get('date')

    if((start_shift_time == None) or (end_shift_time == None)):
        return HttpResponse(json.dumps({'validation':'you missed something', "status":False}), content_type="application/json")



    start_shift_converted_time = datetime.datetime.fromtimestamp(float(start_shift_time))
    end_time_converted_time = datetime.datetime.fromtimestamp(float(end_shift_time))
    date_converted = datetime.datetime.fromtimestamp(float(date))
    fmt = "%Y-%m-%d %H:%M:%S"


    shift = ShiftTime.objects.create(start_shift_time=start_shift_converted_time, end_shift_time=end_time_converted_time, date=date_converted)

    shift.save()
    return HttpResponse(json.dumps({'validation':'added shift successfully', "status": True}), content_type="application/json")


def edit_employee(request):
    jsonobj = json.loads(request.body)
    print jsonobj

    employee_id = jsonobj.get('id')
    team = jsonobj.get('team_id')
    employee_name = jsonobj.get('emp_name')
    email = jsonobj.get('email')
    mob_no = jsonobj.get('mob_no')
    address = jsonobj.get('address')
    position = jsonobj.get('position')
    team_name = jsonobj.get('team_name')

    if employee_name == None:
        return HttpResponse(json.dumps({"validation":"name should not be blank","status":False}), content_type="application/json")

    if team_name == None:
        return HttpResponse(json.dumps({'validation':'please enter team name', "status":False}), content_type="application/json")


    if((len(mobile_no) < 10) or (len(mobile_no) >10)):
        return HttpResponse(json.dumps({'validation':'invalid number', "status":False}), content_type="application/json")


    emp = Employee.objects.get(id = employee_id)

    team_name = Team.objects.get(id = team)

    emp.employee_name = employee_name
    emp.email = email
    emp.mobile_no = mob_no
    emp.address = address
    emp.position = position
    emp.team_name = team_name

    emp.save()

    return HttpResponse(json.dumps({'validation':'Employee updated successfully', "status": True}), content_type="application/json")



def start_break(request):
    jsonobj = json.loads(request.body)
    print jsonobj

    attendance_id = jsonobj.get('attendance_id')
    attendance = AttendanceSheet.objects.get(id = attendance_id)

    break_st=Break.objects.create(attendance=attendance,start_break= datetime.datetime.now())

    break_st.save()
    return HttpResponse(json.dumps({"validation":"start_break  succesfully","status":True}))


def end_break(request):
    jsonobj = json.loads(request.body)
    print jsonobj

    # attendance_id = jsonobj.get('attendance_id')
    # attendance = AttendanceSheet.objects.get(id = attendance_id)

    break_id = jsonobj.get('break_id')

     
    break_ed=Break.objects.get(id=break_id)
    break_ed.end_break = datetime.datetime.now()

    break_ed.save()
    return HttpResponse(json.dumps({"validation":"end_break  succesfully","status":True}))


def calculate_working_hours(request):
    jsonobj = json.loads(request.body)

    attendance_id = jsonobj.get('attendance_id')

    attendance=AttendanceSheet.objects.get(id=attendance_id)
    
    breaks=Break.objects.filter(attendance=attendance)


    #  calculating total break time in an attendance

    total_breaktime = timedelta(days=0,hours=0,minutes=0,seconds=0)   
    for _break in breaks:
        duration = timedelta(days=_break.end_break.day,hours=_break.end_break.hour,minutes=_break.end_break.minute,seconds=_break.end_break.second) - timedelta(days=_break.start_break.day,hours=_break.start_break.hour,minutes=_break.start_break.minute,seconds=_break.start_break.second)
        # print duration
        total_breaktime+= duration
    # print total_breaktime

    # calculating shift hours time

    shift_start=attendance.ShiftTime.start_shift_time
    print shift_start
    shift_end=attendance.ShiftTime.end_shift_time
    print shift_end

    shift_duration = timedelta(days=shift_end.day,hours=shift_end.hour,minutes=shift_end.minute,seconds=shift_end.second) - timedelta(days=shift_start.day,hours=shift_start.hour,minutes=shift_start.minute,seconds=shift_start.second)
    print shift_duration 

    # calculating total_working_time 

    total_working_hours = shift_duration - total_breaktime
    print total_working_hours



    return HttpResponse(json.dumps({"validation":"calculate_break_time successfully","status":True}))

