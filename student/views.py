from django.shortcuts import render

from .forms import ProfileForm
from django.contrib import messages
import re


def profileUpdate(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            em = form.cleaned_data.get('email')
            patt = 'nith.ac.in$'
            if re.search(patt,em) == None:
                messages.info(request,f'use your college email')
                context = {'form': form}
                return render(request, 'profilepage.html',context)
            form.save()
        pass
    else:
        form = ProfileForm()
        context = {'form':form}
        return render(request,'profilepage.html',context) 
