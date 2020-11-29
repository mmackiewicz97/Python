python3 -m venv nazwaWirtualnegoPytona
source nazwaWirt/bin/active
pip3 install django

django-admin startproject nazwaProjektu
cd project
python3 manage.py runserver
python manage.py runserver 0:8000
0 is a shortcut for 0.0.0.0

python3 manage.py startapp aplikacja1
An app is a Web application that does something – e.g., a Weblog system, a database of public records or a small poll app.
A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

widok aplikacji
aplikacja1/views.py

aby stworzony widok był widoczny należy zdefiniować jego URL
project/urls.py
z django.urls import include

testowy - nazwa projektu, bez znaczenia
-> testowy/ -Python package