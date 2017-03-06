import json,datetime,time
from datetime import timedelta
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response , render
# from .forms import  EmployeeForm

from django.contrib.auth import login as django_login


def registration_page(request):
    return render_to_response('html_templates/emp_reg.html')

def team_add_page(request):
    return render_to_response('html_templates/add_team.html')

def edit_employee_page(request):
    return render_to_response('html_templates/edit_employee.html')

def shifttime_page(request):
    return render_to_response('html_templates/add_shift.html')

def breaktime_page(request):
    return render_to_response('html_templates/start_break.html')

def end_break_page(request):
    return render_to_response('html_templates/end_break.html')

def working_hours_page(request):
    return render_to_response('html_templates/working_hours.html')

def timetrackingsystem_page(request):
    return render_to_response('html_templates/timetrackingsystem.html')

def get_user_detail(user):
    emp_detail = Employee.objects.get(user=user)
    print emp_detail

    # for emp_dict in emp_detail:
    #     team = emp_dict.team_name
    #     company =emp_dict.company
    team=emp_detail.team_name
    company=emp_detail.company

    attendance = AttendanceSheet.objects.filter(employee=emp_detail).order_by('-ShiftTime')
   
    if attendance.count() > 0:
        attendance = attendance[0]
    else:
        return HttpResponse(json.dumps({'validation':'your shift is not started!', "status":False}), content_type="application/json")
        
    now = datetime.datetime.now()
    # print now

    if attendance.date.year == now.year and attendance.date.month == now.month and attendance.date.day == now.day: 
        date = attendance.date
    else:
        return HttpResponse(json.dumps({'validation':'your today entery are detected ! please enter its.', "status":False}), content_type="application/json")

    try:
        breaks = Break.objects.get(attendance=shift).order_by('-created')[0]
        print breaks
        break_id = breaks.id
    except Exception as e:
        break_id = None


    queryset = {
                "detail":user,
                "team":team,
                "company":company,
                "shift_time": str(attendance.ShiftTime.start_shift_time) + " to "+str(attendance.ShiftTime.end_shift_time),
                "date":attendance.date,
                "attendence_id":attendance.id,
                "break_id":break_id

            }
 
    return queryset






def add_employee(request):
    print request.body
    print request.POST
    jsonobj = request.POST
    
    address = jsonobj.get('address')
    email = jsonobj.get('email')
    mobile_no= jsonobj.get('mobile_no')
    name =jsonobj.get('name')
    password = jsonobj.get('password')
    team_id = jsonobj.get('team_id')
    position = jsonobj.get('position')
    team_name = jsonobj.get('team_name')
    company = jsonobj.get('company')
    company_id = jsonobj.get('company_id')
    user=jsonobj.get('user')

    # print address , name ,mobile_no,team_name,position,user,password,email


    team = Team.objects.get(id=team_id)
    team.save()

    company = Company.objects.get(id=company_id)
    company.save()


    user = User.objects.create(username=user)
    user.set_password(password)
    user.save()

    employee = Employee.objects.create(user=user,name=name,email=email,mobile_no=mobile_no,position=position,address=address,team_name=team,company=company)
    employee.save()

    return HttpResponse(json.dumps({"validation":"employee added succesfully","status":True}), content_type="application/json")

def login_page(request):
    return render_to_response("html_templates/login.html")

def login(request):
    # jsonobj=json.loads(request.body)
    # print jsonobj

    jsonobj = request.POST

    user_name=jsonobj.get("user_name")
    password=jsonobj.get("password")

    if user_name == None:
        return HttpResponse(json.dumps({'validation':'Enter user name' , "status": False}), content_type="application/json")
    elif password == None:
        return HttpResponse(json.dumps({'validation':'Enter password first' , "status": False}), content_type="application/json")

    print user_name
    user = authenticate(username=user_name,password=password)
    

    if not user:
        return HttpResponse(json.dumps({'validation':'Invalid user', "status": False}), content_type="application/json")
    if not user.is_active:
        return HttpResponse(json.dumps({'validation':'The password is valid, but the account has been disabled!', "status":False}), content_type="application/json")

    django_login(request,user)
    # return HttpResponse(json.dumps({'validation':'Login successfully', "status": True}), content_type="application/json")
    
    queryset = get_user_detail(user)
 
    return render_to_response('html_templates/employee_detail.html',queryset)

def add_team(request):
    # jsonobj = json.loads(request.body)
    jsonobj = request.POST

    team_name = jsonobj.get('team_name')

    team=Team.objects.create(team_name=team_name)
    team.save()

    return HttpResponse(json.dumps({'validation':'team name updated successfully', "status": True}), content_type="application/json")

def add_company(request):
    # jsonobj = json.loads(request.body)
    jsonobj = request.POST

    company = jsonobj.get('company')

    company=Company.objects.create(company=company)
    company.save()

    return HttpResponse(json.dumps({'validation':'company updated successfully', "status": True}), content_type="application/json")



def add_shift(request):
    # jsonobj = json.loads(request.body)
    # print jsonobj

    jsonobj = request.POST

    start_shift_time = jsonobj.get('start_shift_time')
    end_shift_time = jsonobj.get('end_shift_time')
    date = jsonobj.get('date')


    # start_shift_converted_time = datetime.datetime.fromtimestamp(float(start_shift_time))
    # end_time_converted_time = datetime.datetime.fromtimestamp(float(end_shift_time))
    # date_converted = datetime.datetime.fromtimestamp(float(date))

    # fmt = "%Y-%m-%d %H:%M:%S"
    print start_shift_time,end_shift_time,date

    # shift = ShiftTime.objects.create(start_shift_time=start_shift_converted_time, end_shift_time=end_time_converted_time, date=date_converted)
    shift = ShiftTime.objects.create(start_shift_time=start_shift_time, end_shift_time=end_shift_time, date=date)

    shift.save()
    return HttpResponse(json.dumps({'validation':'added shift successfully', "status": True}), content_type="application/json")



def edit_employee(request):
    # jsonobj = json.loads(request.body)
    # print jsonobj

    jsonobj = request.POST

    employee_id = jsonobj.get('employee_id')
    team_id= jsonobj.get('team_id')
    company_id= jsonobj.get('company_id')
    employee_name = jsonobj.get('emp_name')
    email = jsonobj.get('email')
    mob_no = jsonobj.get('mob_no')
    address = jsonobj.get('address')
    position = jsonobj.get('position')
    team_name = jsonobj.get('team_name')
    company = jsonobj.get('company')


    emp = Employee.objects.get(id = employee_id)

    team_name = Team.objects.get(id = team_id)

    company = Team.objects.get(id = company_id)

    emp.employee_name = employee_name
    emp.email = email
    emp.mobile_no = mob_no
    emp.address = address
    emp.position = position
    emp.team_name = team_name
    emp.company = company

    emp.save()

    return HttpResponse(json.dumps({'validation':'Employee updated successfully', "status": True}), content_type="application/json")


def start_break(request):

    jsonobj = request.POST
    print request.POST

  
    attendance_id  = request.POST.get('attendance_id')
    print attendance_id

    # attendance_id = jsonobj.get('attedance_id')

    attendance = AttendanceSheet.objects.get(id=attendance_id)
    print attendance

    breaks = Break.objects.filter(attendance=attendance, start_break__isnull=False,end_break__isnull=True).order_by('-start_break')
    print breaks

    queryset = get_user_detail(request.user)
    print queryset
    
    if not breaks.count() <= 0:
        queryset['messages']="you have already start break! please end your break"
    else:   
        break_st=Break.objects.create(attendance=attendance,start_break= datetime.datetime.now())
        break_st.save()
    
    return render_to_response("html_templates/employee_detail.html",queryset)



def end_break(request):
     # jsonobj = json.loads(request.body)
    # print jsonobj

    print request.POST

    attendence_id = request.POST.get('attendence_id')
    # print "attendence_id: ", attendence_id

    attendance = AttendanceSheet.objects.get(id=attendence_id)
    # print attendance

    breaks = Break.objects.filter(attendance=attendance)
    
    # break_id = jsonobj.get('break_id')

    for _break_ in breaks:
        
        if not _break_.start_break is None:
            break_end=Break.objects.create(attendance=attendance,end_break= datetime.datetime.now())
            break_end.save()
        else:
            return HttpResponse(json.dumps({'validation':'please you before start your break', "status": True}), content_type="application/json")

    queryset = get_user_detail(request.user)
    return render_to_response("html_templates/employee_detail.html",queryset)

    # break_ed=Break.objects.get(id=break_id)
    # break_ed.end_break = datetime.datetime.now()

    # break_ed.save()
    # return render_to_response("html_templates/employee_detail.html",queryset)


def calculate_working_hours(request):
    # jsonobj = json.loads(request.body)
    jsonobj = request.POST

    attendance_id = jsonobj.get('attendance_id')

    attendance=AttendanceSheet.objects.get(id=attendance_id)

    breaks=Break.objects.filter(attendance=attendance).order_by('-start_break')
    print breaks

    if breaks.count > 0:
        _break_ =breaks[0]
        if (_break_.start_break and not _break_.end_break) or (not _break_.start_break and not _break_.end_break):
            return HttpResponse(json.dumps({"validation":"please end your already started break","status":False}))


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

    attendance.working_hours_time=total_working_hours
    attendance.save()

    return HttpResponse(json.dumps({"validation":"calculate_break_time successfully","status":True}))



def show_employee(request):

    all_employees = Employee.objects.all()

    employee_list = []

    for emp in all_employees:
        employee_list.append({"id":emp.id,"user":emp.user.username,"name":emp.name,"email":emp.email,"mobile no":emp.mobile_no,"address":emp.address,"position":emp.position,"team name":emp.team_name.team_name})

    employee_dict = {}
    employee_dict["employee_list"] = employee_list
    return render_to_response('html_templates/show_emp.html',employee_dict)

