from django.db import models
from datetime import  datetime

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class CompanyDatabase(models.Model):
    name = models.ForeignKey(Company,on_delete=models.CASCADE)
    ctc = models.FloatField(default = 0)
    Btech = models.BigIntegerField(default=0)
    Mtech = models.BigIntegerField(default=0)
    Dtech = models.BigIntegerField(default = 0)
    MSC = models.BigIntegerField(default=0)
    total_offers = models.BigIntegerField(default = 0)
    MBA = models.BigIntegerField(default=0)
    #open_dream = models.BooleanField(default = False)
    year = models.BigIntegerField(default = 2022)

class PresentYear(models.Model):
    year = models.IntegerField(default = datetime.now().strftime("%y"),primary_key=True)





