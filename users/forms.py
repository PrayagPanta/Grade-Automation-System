from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ChoiceField( choices=(('S','S') , ('T','T') ) )
    class Meta:
        model = User
        fields = ['username','email','role','password1', 'password2']

class PasswordForm(forms.Form):
    OldPassword = forms.CharField(label="Old Password", max_length=100)
    NewPassword = forms.CharField(label="New Password",max_length=100)
    NewPassword2 = forms.CharField(label="Re-type New Password",max_length=100)
    class Meta:
        fields = ['OldPassword','NewPassword','NewPassword2']
