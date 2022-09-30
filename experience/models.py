from django.db import models

# Create your models here.
class Experience(models.Model):
    choice = [("1", 'Easy'), ("2", 'Medium'), ("3", 'Hard')]
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    drive = models.ForeignKey('drive.Drive', on_delete=models.CASCADE)
    difficulty = models.CharField(choices=choice, default = "1", max_length = 6)
    verdict = models.BooleanField()

    def __str__(self):
        return self.student.fname