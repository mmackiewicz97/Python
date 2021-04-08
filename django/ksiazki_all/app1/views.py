import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Autor
from .models import Ksiazka
from .models import WypozyczonaKsiazka
from .forms import AutorForm
from .forms import KsiazkaForm
from .forms import WypozyczenieForm
from django.contrib import messages

from .forms import LoginForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin


def wyswietl(request):
    autorzy = Autor.objects.all()
    ksiazki = Ksiazka.objects.all()
    wypozyczone = WypozyczonaKsiazka.objects.all()
    return render(request, 'tabela.html', {'autorzy': autorzy, 'ksiazki':ksiazki, 'wypozyczone':wypozyczone})

def dodaj_autora(request, autor):
    autor = autor.split(" ")
    try:
        dodawany = Autor.objects.create(imie=autor[0], nazwisko=autor[1])
        dodawany.save()
    except:
        return HttpResponse("Nie można dodać danego autora.")
    return HttpResponse("Dodano wpis.")

def dodaj_ksiazke(request, ksiazka):
    ksiazka = ksiazka.split(" ")
    try:
        dodawana = Ksiazka.objects.create(tytul=ksiazka[0], wydawnictwo=ksiazka[1], data_wydania=ksiazka[2], klucz_autora=ksiazka[3])
        dodawana.save()
    except:
        return HttpResponse("Nie można dodać danej książki.")
    return HttpResponse("Dodano wpis.")

def dodajAutora(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data #zwraca słownik
            imie = cd.get("imie")
            nazwisko = cd.get("nazwisko")
            Autor.objects.create(imie=imie, nazwisko=nazwisko)
            messages.success(request, "Dodano pomyślnie")
        else:
            messages.warning(request, "Błąd formularza")
    form = AutorForm()
    return render(request, 'dodajAutora.html', {'form':form})


def dodajKsiazke(request):
    if request.method == 'POST':
        form = KsiazkaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data #zwraca słownik
            tytul = cd.get("tytul")
            wydawnictwo = cd.get("wydawnictwo")
            data_wydania = cd.get("example-date-input")
            klucz_autora = cd.get("klucz_autora")
            #autor = Autor.objects.filter(id__exact=klucz_autora)
            Ksiazka.objects.create(tytul=tytul, wydawnictwo=wydawnictwo, data_wydania=data_wydania, klucz_autora=klucz_autora)
            messages.success(request, "Dodano pomyślnie")
        else:
            messages.warning(request, "Błąd formularza")
    form = KsiazkaForm()
    return render(request, 'dodajKsiazke.html', {'form':form})

def welcome(request):
    if request.user.is_authenticated:
        return HttpResponse("Czesc "+ request.user.username)
    else:
        return HttpResponse("Zaloguj sie!")

def appLogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["login"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Zalogowano pomyślnie ;)")
            else:
                messages.warning(request, "Złe hasło ;/")
    if request.user.is_authenticated:
        return render(request, 'loginApp.html')
    else:
        form = LoginForm()
        return render(request, 'loginApp.html', {'form':form})

def appReg(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd.get("login")
            password = cd.get("password")
            email = cd.get("email")
            user, created = User.objects.get_or_create(username=username, email=email)
            if created:
                user.set_password(password)
                user.save()
                return redirect('/app1/login2')
            else:
                messages.warning(request, "Taki użytkownik istnieje!")
    if not request.user.is_authenticated:
        form = RegisterForm()
        return render(request, 'registerApp.html', {'form':form})
    else:
        return redirect('/app1/login2')
@login_required
def wypozyczone(request):
    ilosc_wypozyczonych = WypozyczonaKsiazka.objects.filter(status__exact='w').count()
    liczba_autorow = Autor.objects.count()
    context = {
        'ilosc_wypozyczonych': ilosc_wypozyczonych,
        'liczba_autorow': liczba_autorow
    }
    return render(request, 'wyp.html', context=context)

class WidokWypozyczonychUzytkownika(LoginRequiredMixin, generic.ListView):
    model = WypozyczonaKsiazka
    template_name = 'wypozyczone.html'
    def get_queryset(self):
        return WypozyczonaKsiazka.objects.filter(wypozyczajacy=self.request.user).filter(status__exact='w').order_by('data_zwrotu')

@login_required
@permission_required('app1.can_mark_returned', raise_exception=True)
def wypozycz_ksiazke(request, pk):
    wypozyczona_ksiazka =get_object_or_404(WypozyczonaKsiazka, pk=pk)
    if request.method == 'POST':
        form = WypozyczenieForm(request.POST)
        if form.is_valid():
            wypozyczona_ksiazka.data_zwrotu = form.cleaned_data['data_zwrotu']
            wypozyczona_ksiazka.save()
            #return HttpResponseRedirect(reverse('/app1/moje/'))
            return redirect('/app1/moje/')
    else:
        wstepna_data = datetime.date.today() + datetime.timedelta(days=30)
        form = WypozyczenieForm(initial={'data_zwrotu': wstepna_data})
    context = {
        'form':form,
        'wypozyczona_ksiazka': wypozyczona_ksiazka
    }
    return render(request, 'wypozyczenie_ksiazki.html', context)



