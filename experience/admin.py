from django.contrib import admin
from .models import Experience
# Register your models here.
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('choice','anonymity','student','drive','exp','difficulty','verdict')
    search_fields = ('choice','anonymity','student','drive','exp','difficulty','verdict')

