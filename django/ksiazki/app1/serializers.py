from .models import Autor, Ksiazka
from rest_framework import serializers

class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'imie', 'nazwisko']

class KsiazkaSerializer(serializers.HyperlinkedModelSerializer):
    klucz_autora = serializers.StringRelatedField(many=False)
    class Meta:
        model = Ksiazka
        fields = ['id', 'tytul', 'wydawnictwo', 'data_wydania', 'klucz_autora']