from django.contrib import admin
from .models import Drive, AllowedBranch, Year
# Register your models here.
@admin.register(Drive)
class DriveAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'ctc', 'breakdown', 'job_desc', 'from_date', 'to_date')
    search_fields = ('profile', 'ctc', 'breakdown', 'job_desc', 'from_date', 'to_date')

@admin.register(AllowedBranch)
class AllowedBranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'drive', 'branch')
    search_fields = ('drive', 'branch')

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('year',)
    search_fields = ('year',)