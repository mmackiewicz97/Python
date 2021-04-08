from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'autors', views.AutorViewSet)
router.register(r'ksiazki', views.KsiazkaViewSet)
urlpatterns = [
   # path('', views.wyswietl),
   # path('autor/', views.dodajAutora, name='dodajAutora'),
   # path('ksiazka/', views.dodajKsiazke, name='dodajKsiazke'),
   # path('login/', views.appLogin, name='login'),
   # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   # path('register/', views.appReg, name="register"),
   # path('moje/', views.WidokWypozyczonychUzytkownika.as_view(), name='wypozyczane'),
   # path('ksiazka/<uuid:pk>/wypozycz', views.wypozycz_ksiazke, name='wypozycz_ksiazke'),
   # path('poterminie/', views.poterminie, name='poterminie')
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]