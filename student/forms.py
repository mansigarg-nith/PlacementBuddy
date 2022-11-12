from django.forms import ModelForm
from .models import Student
from django import forms



class ProfileForm(ModelForm):
    fname = forms.CharField(widget=forms.TextInput({'readonly':True}))
    lname = forms.CharField(widget=forms.TextInput({'readonly':True}))
    email = forms.EmailField(widget=forms.EmailInput({'readonly':True}))
    class Meta:
        model = Student
        fields = ['fname','lname','mname','phone','roll','branch','email']
        #fields = '__all__'
