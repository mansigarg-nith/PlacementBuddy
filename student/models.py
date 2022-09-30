from sre_constants import BRANCH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    roll = models.CharField(max_length=100)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)

class Branch(models.Model):
    branch = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)