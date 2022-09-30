from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'fname', 'mname', 'lname', 'email', 'phone', 'roll', 'branch', 'batch')