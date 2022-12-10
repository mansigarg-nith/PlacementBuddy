from django.urls import path

from .views import showDrive,fulldetail
urlpatterns = [
   path('showdrive',showDrive,name = "showdrive"),
   path('drivedetail/<int:id>',fulldetail,name = "drivedetail")
]