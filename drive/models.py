from django.db import models
from student.models import Branch
from company.models import Company
# Create your models here.

class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)

class Drive(models.Model):
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE)
    profile = models.CharField(max_length=100)
    ctc = models.CharField(max_length=100)
    breakdown = models.TextField(max_length=500)
    job_desc = models.TextField(max_length=2000)
    from_date = models.DateField()
    to_date = models.DateField()
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    selected = models.IntegerField()
    def __str__(self):
        return self.profile

class AllowedBranch(models.Model):
    drive = models.ForeignKey(Drive, on_delete=models.CASCADE)
    branch = models.ForeignKey('student.Branch', on_delete=models.CASCADE)