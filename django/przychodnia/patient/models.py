from django.db import models
import uuid

class Pacjent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    data_zabiegu = models.DateField()
