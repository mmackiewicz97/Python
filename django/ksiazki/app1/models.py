from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import date

class Autor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    imie = models.CharField(max_length=200)
    nazwisko = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.id}'

class Ksiazka(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tytul = models.CharField(max_length=200)
    wydawnictwo = models.CharField(max_length=200)
    data_wydania = models.DateField(null=True)
    klucz_autora = models.ForeignKey(Autor, related_name='klucz_autora', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.tytul} - {self.wydawnictwo}. Autor: {self.klucz_autora}'
    class Meta:
        permissions = (("can_add", "Dodanie ksiazki"),)

class WypozyczonaKsiazka(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.SET_NULL, null=True)
    data_zwrotu = models.DateField(null=True, blank=True)
    wypozyczajacy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    STATUS = (
        ('d', 'Dostepna'),
        ('w', 'Wypozyczona')
    )
    status = models.CharField(max_length=1, choices=STATUS, blank=True, default='d')
    def __str__(self):
        return f'{self.id} ({self.ksiazka.tytul})'
    @property
    def po_terminie(self):
        if self.data_zwrotu and date.today() > self.data_zwrotu:
            return True
        return False
    class Meta:
        permissions = (("can_mark_returned", "Wypozyczenie ksiazki"),)



