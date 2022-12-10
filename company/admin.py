from django.contrib import admin
from .models import Company,CompanyDatabase,PresentYear
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(CompanyDatabase)
admin.site.register(PresentYear)


