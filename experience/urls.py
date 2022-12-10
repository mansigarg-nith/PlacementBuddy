from django.urls import path

from . import views

urlpatterns = [
    path('writeExperience', views.writeExperience, name='writeExperience'),
    path('showExperience',views.showExperience,name = "experiencelist"),
    path('fulldetail/<int:id>',views.fulldetail,name = "expdetail"),

]