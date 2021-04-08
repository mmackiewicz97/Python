import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

from rest_framework import viewsets, status
from .serializers import AutorSerializer, KsiazkaSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        autor = get_object_or_404(queryset, id=kwargs.get('id'))
        serializer = self.get_serializer(autor)
        return Response(serializer.data)
    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        autor = get_object_or_404(queryset, id=kwargs.get('id'))
        autor.delete()
        return Response(status=status.HTTP_200_OK)


class KsiazkaViewSet(viewsets.ModelViewSet):
    queryset = Ksiazka.objects.all()
    serializer_class = KsiazkaSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        ksiazka = get_object_or_404(queryset, id=kwargs.get('id'))
        serializer = self.get_serializer(ksiazka)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        ksiazka = get_object_or_404(queryset, id=kwargs.get('id'))
        ksiazka.delete()
        return Response(status=status.HTTP_200_OK)

def wyswietl(request):
    autorzy = Autor.objects.all()
    ksiazki = Ksiazka.objects.all()
    wypozyczone = WypozyczonaKsiazka.objects.all()
    return render(request, 'tabela.html', {'autorzy': autorzy, 'ksiazki':ksiazki, 'wypozyczone':wypozyczone})


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

@permission_required('app1.can_add', raise_exception=True)
def dodajKsiazke(request):
    if request.method == 'POST':
        form = KsiazkaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data #zwraca słownik
            tytul = cd.get("tytul")
            wydawnictwo = cd.get("wydawnictwo")
            data_wydania = cd.get("example-date-input")
            klucz_autora = cd.get("klucz_autora")
            autor = Autor.objects.get(id=klucz_autora)
            Ksiazka.objects.create(tytul=tytul, wydawnictwo=wydawnictwo, data_wydania=data_wydania, klucz_autora=autor)
            messages.success(request, "Dodano pomyślnie")
        else:
            messages.warning(request, "Błąd formularza")
    form = KsiazkaForm()
    return render(request, 'dodajKsiazke.html', {'form':form})


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
        return redirect('/app1/')
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
                return redirect('/app1/login')
            else:
                messages.warning(request, "Taki użytkownik istnieje!")
    if not request.user.is_authenticated:
        form = RegisterForm()
        return render(request, 'registerApp.html', {'form':form})
    else:
        return redirect('/app1/login')

class WidokWypozyczonychUzytkownika(LoginRequiredMixin, generic.ListView):
    model = WypozyczonaKsiazka
    template_name = 'wypozyczone.html'
    def get_queryset(self):
        return WypozyczonaKsiazka.objects.filter(wypozyczajacy=self.request.user).filter(status__exact='w').order_by('data_zwrotu')

@login_required
@permission_required('app1.can_mark_returned', raise_exception=True)
def wypozycz_ksiazke(request, pk):
    wypozyczona_ksiazka =get_object_or_404(WypozyczonaKsiazka, pk=pk)
    if wypozyczona_ksiazka.status == 'w':
        messages.warning(request, "Ta ksiazka jest juz wypożyczona!")
        return redirect('/app1/')
    if request.method == 'POST':
        form = WypozyczenieForm(request.POST)
        if form.is_valid():
            wypozyczona_ksiazka.data_zwrotu = form.cleaned_data['data_zwrotu']
            wypozyczona_ksiazka.wypozyczajacy = request.user
            wypozyczona_ksiazka.status = 'w'
            wypozyczona_ksiazka.save()
            return redirect('/app1/moje/')
    else:
        wstepna_data = datetime.date.today() + datetime.timedelta(days=30)
        form = WypozyczenieForm(initial={'data_zwrotu': wstepna_data})
    context = {
        'form':form,
        'wypozyczona_ksiazka': wypozyczona_ksiazka
    }
    return render(request, 'wypozyczenie_ksiazki.html', context)

@login_required
@permission_required('app1.can_add', raise_exception=True)
def poterminie(request):
    ksiazki = WypozyczonaKsiazka.objects.filter(status__exact='w').order_by('data_zwrotu')
    przeterminowane = []
    for k in ksiazki:
        if k.po_terminie:
            przeterminowane.append(k)
    return render(request, 'po_terminie.html', {'przeterminowane':przeterminowane})


