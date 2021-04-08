from django import forms

class AuthorForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200, required=True)
    surname = forms.CharField(label='Surname', max_length=200, required=True)
