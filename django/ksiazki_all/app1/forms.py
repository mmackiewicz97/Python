from django import forms
from .models import Autor
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class AutorForm(forms.Form):
    imie = forms.CharField(label='Imie', max_length=200, required=True)
    nazwisko = forms.CharField(label='Nazwisko', max_length=200, required=True)

class KsiazkaForm(forms.Form):
    tytul = forms.CharField(label='Tytul', max_length=200, required=True)
    wydawnictwo_class = forms.TextInput(attrs={"class": "form-control"})
    wydawnictwo = forms.CharField(widget=wydawnictwo_class, label='Wydawnictwo', max_length=200, required=True)
    data_wydania = forms.DateField()
    klucz_autora = forms.ModelMultipleChoiceField(queryset=Autor.objects.all())

class LoginForm(forms.Form):
    login_class = forms.TextInput(attrs={"class": "form-control"})
    password_class = forms.PasswordInput(attrs={"class": "form-control"})
    login = forms.CharField(widget=login_class, label="Login", max_length=50, required=True)
    password = forms.CharField(widget=password_class, label="Password", max_length=50, required=True)

class RegisterForm(forms.Form):
    login_class = forms.TextInput(attrs={"class": "form-control"})
    password_class = forms.PasswordInput(attrs={"class": "form-control"})
    email_class = forms.TextInput(attrs={"class": "form-control"})
    login = forms.CharField(widget=login_class, label="Login", max_length=50, required=True)
    password = forms.CharField(widget=password_class, label="Password", max_length=50, required=True)
    email = forms.CharField(widget=login_class, label="Email", max_length=50, required=True)

class WypozyczenieForm(forms.Form):
    data_zwrotu = forms.DateField(help_text="Maksymalnie 30 dni na zwrot")
    def clean_data_zwrotu(self):
        data = self.cleaned_data['data_zwrotu']
        if data < datetime.date.today():
            raise ValidationError(_('Data nie moze byc z przeszlosci'))
        if data > datetime.date.today() + datetime.timedelta(days=30):
            raise ValidationError(_("Data nie moze przekraczac 30 dni"))
        return data


