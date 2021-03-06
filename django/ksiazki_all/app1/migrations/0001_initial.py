# Generated by Django 3.1.3 on 2020-12-08 11:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('2bde7db3-cd9a-4049-95be-87a46a60acb0'), editable=False, primary_key=True, serialize=False)),
                ('imie', models.CharField(max_length=200)),
                ('nazwisko', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ksiazka',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('da67a302-09de-4076-a37d-8808156825f2'), editable=False, primary_key=True, serialize=False)),
                ('tytul', models.CharField(max_length=200)),
                ('wydawnictwo', models.CharField(max_length=200)),
                ('data_wydania', models.DateTimeField()),
                ('klucz_autora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.autor')),
            ],
        ),
    ]
