import json,datetime
from .models import *
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse

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

   team=Team.objects.create(team_name=team_name)
   team.save()

   return HttpResponse(json.dumps({'validation':'team name updated successfully', "status": True}), content_type="application/json")
