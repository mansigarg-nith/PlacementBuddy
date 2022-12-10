from django.shortcuts import render
from .models import Drive 
# Create your views here.
import datetime

def showDrive(request):

    drive = Drive.objects.all()
    date = datetime.date.today()
    return render(request,'drive.html',{'drive':drive,'today':date})


def fulldetail(request,id):
    detail = Drive.objects.get(id = id)
    return render(request,'fulldrive.html',{'drive':detail})