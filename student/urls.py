from django.urls import path

from . import views

urlpatterns = [
    path('profileupdate',views.profileUpdate,name="profileupdate"),
]
