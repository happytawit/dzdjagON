from django import forms

class AddPartner(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    description = forms.CharField(max_length=250, required=False)
    