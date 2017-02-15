import json,datetime
from django.http import HttpResponse
from .models import *

def gettime_schedule(request):
    jsonobj = json.loads(request.body)
    print jsonobj

    start_time = jsonobj.get('start_time')
    end_time = jsonobj.get('end_time')

    started_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(start_time))).timedelta()
    ended_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(end_time)))

    get_time_diff = ended_time - started_time
    print get_time_diff

    time = Worktime_Record.objects.create(start_time=start_time ,end_time=end_time)

    time.save()
    return HttpResponse(json.dumps({'validation':'get time difference is succesfully','status':True }))
