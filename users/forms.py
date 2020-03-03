from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField( choices=(('S','S') , ('T','T') ) )
    class Meta:
        model = User
        fields = ['username','email','role','password1', 'password2']
