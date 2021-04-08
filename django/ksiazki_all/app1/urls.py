from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.wyswietl),
    path('dodA/<autor>', views.dodaj_autora),
    path('dodK/<ksiazka>', views.dodaj_ksiazke),
    path('autor/', views.dodajAutora, name='dodajAutora'),
    path('ksiazka/', views.dodajKsiazke, name='dodajKsiazke'),
    path('welcome/', views.welcome, name="welcome"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login2/', views.appLogin, name='login2'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.appReg, name="register"),
    path('wyp/', views.wypozyczone, name="wypozyczone"),
    path('moje/', views.WidokWypozyczonychUzytkownika.as_view(), name='wypozyczane'),
    path('ksiazka/<uuid:pk>/wypozycz', views.wypozycz_ksiazke, name='wypozycz_ksiazke'),
]