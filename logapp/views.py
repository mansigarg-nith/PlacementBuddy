from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['Password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            redirect('login')
    return render(request, 'studentlogin.html')