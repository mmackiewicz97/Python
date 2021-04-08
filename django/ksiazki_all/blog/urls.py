from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('dodaj/', views.dodajpost, name='dodajpost'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]