from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import UserRegistrationForm
from django.contrib import messages
import re




# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            return HttpResponseRedirect(request.path_info)
    return render(request, 'studentlogin.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            em = form.cleaned_data.get('email')
            patt = 'nith.ac.in$'
            if re.search(patt,em) == None:
                messages.info(request,f'use your college email')
                context = {'form': form}
                return render(request, 'studentregister.html',context)
            form.save()

            #messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('/user/login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'studentregister.html', context)

        
   