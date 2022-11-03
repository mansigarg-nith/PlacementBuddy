from re import template
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login', views.login, name='studentlogin'),
    path('register',views.register,name = 'studentregister'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name = "reset_password.html"),name = 'reset_password'),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name = "reset_password_sent.html"),name = "password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name = "reset_password_form.html"),name = 'password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name = "reset_password_done.html"),name = 'password_reset_complete'),


]
