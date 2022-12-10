from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'homepage.html')

def dashboard(request):
    context = {'user':request.user}
    return render(request,'navbar.html',context)