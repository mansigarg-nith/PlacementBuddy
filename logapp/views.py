from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import auth
from .forms import UserRegistrationForm
from django.contrib import messages
import re
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from .tokens import account_activation_token



# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = auth.authenticate(username = username, password=password)
        if user is not None:
            #print(user.is_active)
            #context = {'user' : request.user}
            auth.login(request,user)

            return redirect('/dashboard')
        else:
            #print(False)
            print("your credentials are wrong")
            return HttpResponseRedirect(request.path_info)
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            em = form.cleaned_data.get('email')
            patt = 'nith.ac.in$'
            if re.search(patt,em) == None:
                messages.info(request,f'use your college email')
                context = {'form': form}
                return render(request, 'login.html',context)
            #form.save()
            user = form.save(commit=False)
            user.is_active = False # Deactivate account till it is confirmed
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))


            #return redirect('login')

            #messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('/user/login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def view_logout(request):
    logout(request)
    return redirect("/")


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('account_activation_email.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
            received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        print('Your account have been confirmed.')
        user.save()
        messages.success(request, ('Your account have been confirmed.'))
        return redirect('/user/login')
    else:
        messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
        return redirect('homepage')
        

        
   