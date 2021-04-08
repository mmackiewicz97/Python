from django import forms

class PacjentForm(forms.Form):
    imie = forms.CharField(label='Imie', max_length=200, required=True)
    nazwisko = forms.CharField(label='Nazwisko', max_length=200, required=True)
    data_zabiegu = forms.DateField()
