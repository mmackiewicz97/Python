# Generated by Django 3.1.3 on 2020-12-23 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20201222_2030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wypozyczonaksiazka',
            options={'permissions': (('can_mark_returned', 'Wypozyczenie ksiazki'),)},
        ),
    ]