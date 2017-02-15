import json,datetime
from django.http import HttpResponse
from .models import *


# def gettime_schedule(request):
#     jsonobj = json.loads(request.body)
#     print jsonobj

#     start_time = jsonobj.get('start_time')
#     end_time = jsonobj.get('end_time')

#     started_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(start_time))).timedelta()
#     ended_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(end_time)))

#     get_time_diff = ended_time - started_time
#     print get_time_diff

#     time = Worktime_Record.objects.create(start_time=start_time ,end_time=end_time)

#     time.save()
#     return HttpResponse(json.dumps({'validation':'get time difference is succesfully','status':True }))


def add_shift(request):
    jsonobj = json.loads(request.body)
    print jsonobj

    start_shift_time = jsonobj.get('start_shift_time')
    end_shift_time = jsonobj.get('end_shift_time')
    date = jsonobj.get('date')


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



def break_time(request):
    jsonobj = json.loads(request.body)
    print jsonobj

    attendance_id = jsonobj.get('attendance_id')
    break_time = jsonobj.get('break_time')
    break_type = jsonobj.get('break_type')

    attendance = AttendanceSheet.objects.get(id = attendance_id)

    break_time =Break.objects.create(attendance=attendance_id,break_time=break_time,break_type=break_type)

    break_time.attendance = final_attendance
    break_time.break_time = breakTime
    break_time.break_type = breakType


    break_time.save()
    return HttpResponse(json.dumps({"validation":"break time added succesfully","status":True}))




