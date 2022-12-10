from django.contrib import admin
from django.urls import path
from . import views
  
urlpatterns = [
    path('getdata/<int:year>', views.HomeView.as_view(),name ="getdata"),
    # path('test-api', views.get_data),
    path('api/<int:year>', views.ChartData.as_view(),name = "api"),
    path('getfulldata',views.companyData.as_view(),name = "getfulldata"),
    path('resources',views.resources,name="resources")
]