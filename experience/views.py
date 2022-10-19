from django.shortcuts import render
from drive.models import Drive
import experience
from student.models import Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def writeExperience(request):
    if request.method == 'POST':
        user = request.user
        anonymity = request.POST.get('user_identity1')
        company_name = request.POST.get('user_company_name')
        role = request.POST.get('user_role')
        difficulty1 = request.POST.get('user_difficulty1')
        difficulty2 = request.POST.get('user_difficulty2')
        difficulty3 = request.POST.get('user_difficulty3')
        difficulty = 1
        if difficulty1 == 1:
            difficulty = 1
        elif difficulty2 == 1:
            difficulty = 2
        else:
            difficulty = 3

        experience = request.POST.get('user_interview_experience')
        result = request.POST.get('user_final_result')
        year = request.POST.get('user_year')
        student = Student.objects.get(user=user)
        drive = Drive.objects.get(company=company_name, year=year)
        exp = experience(student = student, anonymity = anonymity, drive = drive, difficulty = difficulty, exp = experience, verdict = result)
        exp.save()
        messages.success(request,'Data has been submitted')
        return render(request, 'experience/writeExperience.html')
    return render(request, 'expform.html')