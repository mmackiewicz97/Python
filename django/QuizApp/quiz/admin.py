from django.contrib import admin
import adminactions.actions as actions
from django.contrib.admin import site
from .models import Quiz, Pytanie


class AdminQuiz(admin.ModelAdmin):
    list_display = ('nazwa', 'opis', 'tworca')
    list_filter = ('tworca',)

admin.site.register(Quiz, AdminQuiz)


class AdminPytanie(admin.ModelAdmin):
    list_display = ('pytanie', 'quiz')
    list_filter = ('quiz',)

admin.site.register(Pytanie, AdminPytanie)

actions.add_to_site(site)
