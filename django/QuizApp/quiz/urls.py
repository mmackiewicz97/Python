from django.urls import path
from .views import *

urlpatterns = [
    path('', QuizList.as_view(), name='index'),
    path('quiz/<id>', dany_quiz, name='dany_quiz'),
    path('podsumowanie/', podsumowanie_quizu, name='podsumowanie'),
    path('dodajquiz/', dodaj_quiz, name='dodaj_quiz'),
    path('dodajpytanie/<id>', dodaj_pytanie, name='dodaj_pytanie'),
    path('zaloguj/', zaloguj, name='zaloguj'),
    path('zarejestruj/', zarejestruj, name='zarejestruj'),
    path('wyloguj/', wyloguj, name='wyloguj'),
    path('usunpyt/<pk>', PytanieDelete.as_view(), name='usun_pytanie'),
    path('usunquiz/<pk>', QuizDelete.as_view(), name='usun_quiz'),
    path('edytujquiz/<id>', edytuj_quiz, name='edytuj_quiz'),
    path('edytujpytanie/<id>', edytuj_pytanie, name='edytuj_pytanie'),
    path('moje/', moje_quizy, name='moje_quizy'),
]
