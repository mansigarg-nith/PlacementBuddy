from django.contrib import admin
from .models import Branch, Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'fname', 'mname', 'lname', 'email', 'phone', 'roll', 'branch')

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch', 'batch')