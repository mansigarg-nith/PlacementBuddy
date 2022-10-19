from django.urls import path

from . import views

urlpatterns = [
    path('writeExperience', views.writeExperience, name='writeExperience')

]