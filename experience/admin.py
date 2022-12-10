from django.contrib import admin
from .models import Experience
# Register your models here.
# @admin.register(Experience)
# class ExperienceAdmin(admin.ModelAdmin):
#     list_display = ('anonymity','student','difficulty','exp','verdict',"year")
#     #search_fields = ('anonymity','student','difficulty','exp','verdict',"year")
admin.site.register(Experience)
