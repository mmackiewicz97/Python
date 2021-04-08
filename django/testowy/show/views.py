from django.shortcuts import render
from django.http import HttpResponse
from .models import Computer, Author
from .forms import AuthorForm
from django.contrib import messages

def index(request):
    return HttpResponse("Witaj, możesz wyświetlić swój tekst poprzez dopisanie go do adresu strony.")

def funkcja(request, text):
    context = {'text': text}
    return render(request, 'index.html', context)

def computers(request):
    computers = Computer.objects.all()
    return render(request, 'computers.html', {'computers': computers})
def reqargm(request):
    val = request.GET.get('myArg', '')
    return HttpResponse(val)

# def addAuthorForm(request):
#     form = AuthorForm()
#     return render(request, 'addAuthor.html', {'form':form})
def addAuthorForm(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data #zwraca słownik
            name = cd.get("name")
            surname = cd.get("surname")
            Author.objects.create(name=name, surname=surname)
            messages.success(request, "Dodano pomyślnie")
        else:
            messages.warning(request, "Błąd formularza")
            #return HttpResponse("Dodano pomyślnie")
        #return HttpResponse('Błąd formularza')
    form = AuthorForm()
    return render(request, 'addAuthor.html', {'form':form})