from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name="index"),
   # path('index', views.index,name="index"),
    path('refresh', views.refresh,name="refresh"),
    path('highestctc/<int:pk>', views.highestctc,name="highestctc"),
    path('highestbase', views.highestbase,name="highestbase"),
    path('highestoffers/<int:pk>', views.highestoffers,name="highestoffers"),
    path('cgpa', views.cgpa,name="cgpa"),
    path('UpdateYear', views.change_year,name="UpdateYear"),
    path('statistics',views.statistics,name = "statistics"),
    path('companydetail/<int:pk>',views.companydetail,name= "companydetail"),


    
]
