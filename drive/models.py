from django.db import models
from student.models import Branch
# Create your models here.
class Drive(models.Model):
    profile = models.CharField(max_length=100)
    ctc = models.CharField(max_length=100)
    breakdown = models.TextField(max_length=500)
    job_desc = models.TextField(max_length=2000)
    from_date = models.DateField()
    to_date = models.DateField()
    year = models.ForeignKey('Year', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class AllowedBranch(models.Model):
    drive = models.ForeignKey('Drive', on_delete=models.CASCADE)
    branch = models.ForeignKey('student.Branch', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)