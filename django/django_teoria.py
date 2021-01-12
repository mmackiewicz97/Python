# python3 -m venv nazwaWirtualnegoPytona
# source nazwaWirt/bin/active
# pip3 install django
#
# django-admin startproject nazwaProjektu
# cd project
# python3 manage.py runserver
# python manage.py runserver 0:8000
# 0 is a shortcut for 0.0.0.0
#
# python3 manage.py startapp aplikacja1
# An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app.
# A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.
#
# widok aplikacji
# aplikacja1/views.py
#
# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Autor
# def index(request):
#     return HttpResponse("Hello!")
# def wyswietl(request):
#     autorzy = Autor.objects.all()
#     return render(request, 'tabela.html', {'autorzy': autorzy, 'ksiazki':ksiazki})

# aby stworzony widok był widoczny należy zdefiniować jego URL
# aplikacja1/urls.py
# lub globalnie w głównym url

# z django.urls import include
# dodanie urls aplikacji do glownego url
# dodanie wtedy pliku urls.py do aplikacji
#
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.index, name="index"),
#     path('render/', views.wyswietl, name="wyswietl"),
# ]

# testowy - nazwa projektu, bez znaczenia
# -> testowy/ -Python package

# python3 manage.py makemigrations (app)
# przygotowanie plików do migracji, tworzenie tabel

# python3 manage.py migrate
# migrowanie, jeżeli czegoś w bazie brakuje zostanie to utworzone

# python3 manage.py createsuperuser

# lista INSTALLED_APPS w pliku settings.py
# model jest klasą reprezentującą tabelę w bazie danych
# model tworzy się w pliku models.py
# import uuid
#
# class Autor(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
#     imie = models.CharField(max_length=200)

# dodanie modelu do admin.py
# from .models import Ksiazka
# admin.site.register(Autor)

# stworzenie widoku views.py,
# dodanie urla urls.py,
# stworzenie szablonu szablon.html
# w settings.py dodanie ścieźki do templates do DIRS

# from django.contrib import messages
# base.html, rozszerzanie,
# bootstrap