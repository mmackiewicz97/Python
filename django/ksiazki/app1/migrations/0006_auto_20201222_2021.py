# Generated by Django 3.1.3 on 2020-12-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_wypozyczonaksiazka_wypozyczajacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ksiazka',
            name='data_wydania',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='wypozyczonaksiazka',
            name='data_zwrotu',
            field=models.DateField(blank=True, null=True),
        ),
    ]
