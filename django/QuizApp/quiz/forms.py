from django import forms


class ZalogujForm(forms.Form):
    loginClass = forms.TextInput(attrs={'class': 'form-control'})
    hasloClass = forms.PasswordInput(attrs={'class': 'form-control'})
    login = forms.CharField(widget=loginClass, label="Login", max_length=50, required=True)
    haslo = forms.CharField(widget=hasloClass, label="Hasło", max_length=50, required=True)


class ZarejestrujForm(forms.Form):
    loginClass = forms.TextInput(attrs={'class': 'form-control'})
    hasloClass = forms.PasswordInput(attrs={'class': 'form-control'})
    login = forms.CharField(widget=loginClass, label="Login", max_length=50, required=True)
    imie = forms.CharField(widget=loginClass, label="Imię", max_length=30, required=True)
    nazwisko = forms.CharField(widget=loginClass, label="Nazwisko", max_length=30, required=True)
    email = forms.CharField(widget=loginClass, label="E-mail", max_length=250, required=True)
    haslo = forms.CharField(widget=hasloClass, label="Hasło", max_length=50, required=True)


class QuizForm(forms.Form):
    nazwaClass = forms.TextInput(attrs={'class': 'form-control'})
    nazwa = forms.CharField(widget=nazwaClass, label="Nazwa Quizu", max_length=50)
    opis = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 10}))


class PytanieForm(forms.Form):
    nazwaClass = forms.TextInput(attrs={'class': 'form-control'})
    pytanie = forms.CharField(widget=nazwaClass, label="Quizowe pytanie", max_length=500)
    opcja1 = forms.CharField(widget=nazwaClass, label="Odpowiedź 1", max_length=500)
    opcja2 = forms.CharField(widget=nazwaClass, label="Odpowiedź 2", max_length=500)
    opcja3 = forms.CharField(widget=nazwaClass, label="Odpowiedź 3", max_length=500, required=False)
    opcja4 = forms.CharField(widget=nazwaClass, label="Odpowiedź 4", max_length=500, required=False)
    odpowiedz = forms.IntegerField(min_value=1, max_value=4, label="Numer poprawnej odpowiedzi", initial=1)
