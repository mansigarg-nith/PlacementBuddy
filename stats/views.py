from django.shortcuts import render
from django.views.generic import View
   
from rest_framework.views import APIView
from rest_framework.response import Response
from company.models import *
from .serializers import companyserializers

# Create your views here.
class HomeView(View):
    def get(self, request,year):
        print(year,"yeas")
        return render(request, 'indexstats.html',{"year":year})



# using rest framework classes

class companyData(APIView):
    def get(self,request):
        data = CompanyDatabase.objects.all()
        serliazer = companyserializers(data,many = True)
        return Response(serliazer.data)







class ChartData(APIView):
    authentication_classes = []
    permission_classes = []



   
    def get(self,request,year):
        #print(pk)
        data = CompanyDatabase.objects.filter(year = year)
        serliazer = companyserializers(data,many = True)
        #print(serliazer.data)



        return Response(serliazer.data)




def resources(request):
    return render(request,'resources.html')
    
