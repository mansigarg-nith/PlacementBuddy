from django.shortcuts import render

# Create your views here.
def home(request):
    print('yes')
    return render(request,'homepage.html')