from enum import unique
from turtle import textinput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101,widget=forms.TextInput(attrs={'class':'input'}))
    last_name = forms.CharField(max_length=101,widget=forms.TextInput(attrs={'class':'input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'input'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs) -> None:
        super(UserRegistrationForm,self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class" ] = 'input'
        self.fields["password1"].widget.attrs["class" ] = 'input'
        self.fields["password2"].widget.attrs["class" ] = 'input'
         