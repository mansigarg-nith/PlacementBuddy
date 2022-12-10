from django.shortcuts import render,redirect
from .forms import ProfileForm
from django.contrib import messages
import re
from django.contrib.auth.models import User
from .models import Student


def profileUpdate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            profiledata = Student.objects.filter(user_id = request.user.id).exists()
            form = ProfileForm(data = request.POST)
            print(form)
            # if profiledata is not None:
            #     print(profiledata)
            #     form = ProfileForm(instance=profiledata) 
            if form.is_valid():
                if profiledata:
                    a = Student.objects.get(user_id = request.user.id)
                    form = ProfileForm(data=request.POST,instance=a)
                else:
                    form.instance.user = request.user
                #form.instance.user = request.user
                form.save()
                return redirect('dashboard')
            else:
                print("no")
                print(form)
                

        else:
            user_data = request.user
            data = {'fname':user_data.first_name,'lname':user_data.last_name,'email':user_data.email}
            profiledata = Student.objects.filter(user_id = request.user.id).exists()
            form = ProfileForm(data)
            if profiledata:
                a = Student.objects.get(user_id = request.user.id)
                form = ProfileForm(instance=a) 
            context = {'form':form,"user":request.user}
            return render(request,'profilepage.html',context)
         
    
