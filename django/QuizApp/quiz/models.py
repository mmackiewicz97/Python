from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    tworca = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    nazwa = models.CharField(max_length=100)
    opis = models.CharField(max_length=1000)

    def __str__(self):
        return self.nazwa


class Pytanie(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    pytanie = models.CharField(max_length=500)
    odpowiedz = models.IntegerField()
    opcja1 = models.CharField(max_length=500)
    opcja2 = models.CharField(max_length=500)
    opcja3 = models.CharField(max_length=500, blank=True)
    opcja4 = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.pytanie
