from http.client import HTTPResponse
from django.shortcuts import render, redirect
from drive.models import Drive
from .models import *
from company.models import Company
from student.models import Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ckeditor.fields import RichTextField

# Create your views here.
# @login_required(login_url='logapp/studentlogin.html')
def writeExperience(request):
    if not request.user.is_authenticated:
        return render(request, 'studentlogin.html')
    
    if request.method == 'POST':
        user = request.user
        anonymity = request.POST.get('user_identity')
        if anonymity == "Reveal":
            anonymity = False
        else:
            anonymity = True
        company_name = request.POST.get('user_company_name')
        #role = request.POST.get('user_role')
        difficulty = request.POST.get('difficulty')
        
            
        print(difficulty)


        experience = RichTextField()
        experience = request.POST.get('user_interview_experience')
        result = request.POST.get('user_final_result')
        if result == "Selected":
            result = True
        else:
            result = False
        company_name = company_name.capitalize()
        year = request.POST.get('user_year')
        student = Student.objects.get(user=user)
        company = Company.objects.all().values()
        if company_name not in company:
            Company.objects.create(name = company_name)
            company = Company.objects.get(name = company_name)
        else:
            company = Company.objects.get(name = company_name)


        #drive = Drive.objects.get(company=company_name, year=year)
        exp = Experience(student = student, anonymity = anonymity, difficulty = difficulty,company = company,year=year,exp = experience, verdict = result)
        exp.save()
        messages.success(request,'Data has been submitted')
        return render(request, 'expform.html')
   
    return render(request, 'expform.html')


def showExperience(request):
    if request.method == "POST":
        company = request.POST["company"]
        company = company.capitalize()
        result = request.POST["result"]
        batch = request.POST["year"]
        if company == "":
            if result == "Both":
                exp = Experience.objects.filter(year = batch)
            else:
                if result == "selected":
                    exp = Experience.objects.filter(year = batch,verdict = True)
                else:
                    exp = Experience.objects.filter(year = batch,verdict = False)
        else:
            if result == "Both":
                exp = Experience.objects.filter(company = company,year = batch)
            else:
                if result == "selected":
                    exp = Experience.objects.filter(company = company,year = batch,verdict = True)
                else:
                    exp = Experience.objects.filter(company = company,year = batch,verdict = False)

        
    
        return render(request,'experience_list.html',{'exp':exp})
    exp = Experience.objects.all()
    context = {'exp':exp}
    #print(exp.values()[0])

    return render(request,'experience_list.html',context)


def fulldetail(request,id):
    expdetail = Experience.objects.get(id = id)
    return render(request,'fulldetail.html',{'expdetail':expdetail})

        
