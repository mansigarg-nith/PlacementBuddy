from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Experience(models.Model):
    choice = [("1", 'Easy'), ("2", 'Medium'), ("3", 'Hard')]
    anonymity = models.BooleanField(default=False)
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    drive = models.ForeignKey('drive.Drive', on_delete=models.CASCADE)
    exp = RichTextField()
    difficulty = models.CharField(choices=choice, default = "1", max_length = 6)
    verdict = models.BooleanField()

    def _str_(self):
        return self.student.fname