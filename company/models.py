from django.db import models
from drive.models import Drive
# Create your models here.
class Company(models.Model):
    drive = models.ForeignKey('drive.Drive', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    # 0 - IT, 1 - Core
    type = models.BooleanField()
    selected = models.IntegerField()

    def __str__(self):
        return self.name

