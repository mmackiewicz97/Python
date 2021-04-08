from django.shortcuts import render, redirect
from .models import Quiz, Pytanie
from .forms import ZalogujForm, ZarejestrujForm, QuizForm, PytanieForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class QuizList(ListView):
    template_name = 'index.html'
    model = Quiz


class PytanieDelete(DeleteView):
    model = Pytanie
    template_name = "usunpytanie.html"
    success_url = reverse_lazy('moje_quizy')


class QuizDelete(DeleteView):
    model = Quiz
    template_name = "usunquiz.html"
    success_url = reverse_lazy('moje_quizy')


@login_required
def moje_quizy(request):
    user = request.user
    quizy = Quiz.objects.filter(tworca=user)
    return render(request, 'mojequizy.html', {'quizy': quizy})


@login_required
def edytuj_pytanie(request, id):
    pytanie = Pytanie.objects.get(id=id)
    if request.method == 'POST':
        form = PytanieForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            pytanie.pytanie = cd.get("pytanie")
            pytanie.opcja1 = cd.get("opcja1")
            pytanie.opcja2 = cd.get("opcja2")
            pytanie.opcja3 = cd.get("opcja3")
            pytanie.opcja4 = cd.get("opcja4")
            pytanie.odpowiedz = cd.get("odpowiedz")
            pytanie.save()
            messages.success(request, "Edytowano pytanie!")
            return redirect("edytuj_quiz", pytanie.quiz.id)
        else:
            messages.warning(request, "Błąd formularza!")
    form = PytanieForm(initial={'pytanie': pytanie.pytanie, 'opcja1': pytanie.opcja1, 'opcja2': pytanie.opcja2,
                                'opcja3': pytanie.opcja3, 'opcja4': pytanie.opcja4, 'odpowiedz': pytanie.odpowiedz})
    return render(request, 'edytujpytanie.html', {'form': form})


@login_required
def edytuj_quiz(request, id):
    quiz = Quiz.objects.get(id=id)
    pytania = Pytanie.objects.filter(quiz=quiz)
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            quiz.nazwa = cd.get("nazwa")
            quiz.opis = cd.get("opis")
            quiz.save()
            messages.success(request, "Edytowano quiz!")
            return redirect("index")
        else:
            messages.warning(request, "Błąd formularza!")
    form = QuizForm(initial={'tworca': quiz.tworca, 'nazwa': quiz.nazwa, 'opis': quiz.opis})
    return render(request, 'edytujquiz.html', {'form': form, 'pytania': pytania, 'id':id})


@login_required
def dodaj_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data  # zwraca słownik
            nazwa = cd.get("nazwa")
            opis = cd.get("opis")
            user = request.user
            quiz = Quiz.objects.create(nazwa=nazwa, tworca=user, opis=opis)
            messages.success(request, "Utworzono quiz!")
            return redirect("dodaj_pytanie", id=quiz.id)
        else:
            messages.warning(request, "Błąd formularza")
    form = QuizForm()
    return render(request, 'dodajquiz.html', {'form': form})


@login_required
def dodaj_pytanie(request, id):
    quiz = Quiz.objects.get(id=id)
    if request.method == 'POST':
        form = PytanieForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data  # zwraca słownik
            pytanie = cd.get("pytanie")
            opcja1 = cd.get("opcja1")
            opcja2 = cd.get("opcja2")
            opcja3 = cd.get("opcja3")
            opcja4 = cd.get("opcja4")
            odpowiedz = cd.get("odpowiedz")
            Pytanie.objects.create(quiz=quiz, pytanie=pytanie, opcja1=opcja1, opcja2=opcja2, opcja3=opcja3,
                                   opcja4=opcja4, odpowiedz=odpowiedz)
            messages.success(request, "Dodano pytanie pomyślnie")
            return redirect("dodaj_pytanie", id=quiz.id)
        else:
            form = PytanieForm(initial={'quiz': quiz})
            messages.warning(request, "Błąd formularza")
            return render(request, 'dodajpytanie.html', {'id': id, 'form': form})

    else:
        form = PytanieForm(initial={'quiz': quiz})
        return render(request, 'dodajpytanie.html', {'id': id, 'form': form})


def dany_quiz(request, id):
    if request.method == "POST":
        zadane_pytanie = Pytanie.objects.get(id=int(request.POST['pytanie']))
        if 'name' in request.POST:
            if zadane_pytanie.odpowiedz == int(request.POST.get('name')):
                request.session['wynik'] += 1
            else:
                request.session['zle_odp'][zadane_pytanie.pytanie] = [zadane_pytanie.id]
            if request.POST.get("next") == "puste":
                return redirect("podsumowanie")
            id_pytania = int(request.POST['next'])
            pytanie = Pytanie.objects.filter(quiz__id=id, id=id_pytania)[0]
            sprawdzenie = Pytanie.objects.filter(quiz__id=id).order_by('id').last()
            if pytanie.id is not sprawdzenie.id:
                next = Pytanie.objects.filter(quiz__id=id, id__gt=pytanie.id).order_by('id').first()
                return render(request, 'quiz.html', {'id_quizu': id, 'pytanie': pytanie, 'next': next.id})
            else:
                return render(request, 'quiz.html', {'id_quizu': id, 'pytanie': pytanie, 'next': "puste"})
        else:
            messages.warning(request, "Zaznacz odpowiedź!")
            next = request.POST['next']
            return render(request, 'quiz.html', {'id_quizu': id, 'pytanie': zadane_pytanie, 'next': next})

    else:
        request.session['wynik'] = 0
        request.session['zle_odp'] = {}
        try:
            pytanie = Pytanie.objects.filter(quiz__id=id).first()
            next = Pytanie.objects.filter(quiz__id=id, id__gt=pytanie.id).order_by('id').first()
            if next is not None:
                return render(request, 'quiz.html', {'id_quizu': id, 'pytanie': pytanie, 'next': next.id})
            else:
                return render(request, 'quiz.html', {'id_quizu': id, 'pytanie': pytanie, 'next': "puste"})
        except:
            messages.warning(request, "W danym quizie nie ma pytań!")
            return redirect('dodaj_pytanie', id=id)


def podsumowanie_quizu(request):
    return render(request, 'podsumowanie.html')


def zaloguj(request):
    if request.method == 'POST':
        form = ZalogujForm(request.POST)
        if form.is_valid():
            username = request.POST["login"]
            password = request.POST["haslo"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Zostałeś zalogowany!")
            else:
                messages.warning(request, "Błąd logowania! Popraw dane i spróbuj ponownie.")
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = ZalogujForm()
        return render(request, 'zaloguj.html', {'form': form})


def zarejestruj(request):
    if request.method == 'POST':
        form = ZarejestrujForm(request.POST)
        if form.is_valid():
            login = request.POST["login"]
            imie = request.POST["imie"]
            nazwisko = request.POST["nazwisko"]
            email = request.POST["email"]
            haslo = request.POST["haslo"]
            user, created = User.objects.get_or_create(username=login, email=email, first_name=imie, last_name=nazwisko)
            if created:
                user.set_password(haslo)
                user.save()
                messages.success(request, "Zarejestrowano pomyślnie! Możesz się już zalogować.")
                return redirect('zaloguj')
            else:
                messages.warning(request, "Użytkownik istnieje w bazie!")
    if not request.user.is_authenticated:
        form = ZarejestrujForm()
        return render(request, 'zarejestruj.html', {'form': form})
    else:
        redirect('index')


def wyloguj(request):
    logout(request)
    return redirect('index')
