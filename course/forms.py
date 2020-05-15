from django import forms
from .models import Marks

class NameForm(forms.Form):
    SID = forms.CharField(label="Student's ID", max_length=100)

class NameForm2(forms.Form):
    SID = forms.CharField(label="Student's ID", max_length=100)
    Qno = forms.CharField(label="Question Number",max_length=4)

class UpdateForm(forms.Form):
    NewMarks = forms.IntegerField(label="Enter the Updated Mark")


class AddForm(forms.ModelForm):
    Qno = forms.CharField(label="Enter the question number for the answer",max_length=4)
    Marks = forms.IntegerField(label="Enter the Marks")

    class Meta:
        model = Marks
        fields = ['Qno', 'Marks']
