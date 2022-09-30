from django.contrib import admin
from .models import Company
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'selected')
    list_filter = ('type', 'selected')
    search_fields = ('name',)

