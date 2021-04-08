from django.contrib import admin
from .models import Autor
from .models import Ksiazka
from .models import WypozyczonaKsiazka

import adminactions.actions as actions
from django.contrib.admin import site

admin.site.register(Autor)
#admin.site.register(Ksiazka)
class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'wydawnictwo', 'data_wydania', 'klucz_autora')
admin.site.register(Ksiazka, KsiazkaAdmin)

class WypozyczonaKsiazkaAdmin(admin.ModelAdmin):
    list_filter = ('status', 'data_zwrotu', 'wypozyczajacy')
admin.site.register(WypozyczonaKsiazka, WypozyczonaKsiazkaAdmin)

actions.add_to_site(site)
