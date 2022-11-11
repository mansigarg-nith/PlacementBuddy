from django.forms import ModelForm
from .models import Student



class ProfileForm(ModelForm):
    class Meta:
        model = Student
        fields = ['phone','roll','branch']
