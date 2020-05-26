from django import forms


class ComplaintForm(forms.Form):
    Subject = forms.CharField(max_length=100)
    Complaint = forms.CharField(label="Complaint", max_length=100)
    class Meta:
        fields = ['Subject','Complaint']
