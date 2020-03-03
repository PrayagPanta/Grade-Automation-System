from django import forms
from .models import Marks

class NameForm(forms.Form):
    SID = forms.CharField(label="Student's ID", max_length=100)

class AddForm(forms.ModelForm):
    Qno = forms.CharField(label="Enter the question Number",max_length=4)
    Marks = forms.IntegerField(label="Enter the Marks")

    class Meta:
        model = Marks
        fields = ['Qno', 'Marks']
