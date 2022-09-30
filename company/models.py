from email.policy import default
from django.db import models
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    # 0 - IT, 1 - Core
    type = models.BooleanField(default=0)

    def __str__(self):
        return self.name

