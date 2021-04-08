from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('//<text>', views.funkcja),
    path('computers/', views.computers, name="computers"),
    path('reqarg/', views.reqargm, name="reqargm"),
    path('author/', views.addAuthorForm, name='addAuthorForm'),
]