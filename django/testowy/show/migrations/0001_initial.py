# Generated by Django 3.1.3 on 2020-12-08 10:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('8a51c35a-8f13-469c-ae75-cb68c64b97f8'), editable=False, primary_key=True, serialize=False)),
                ('manufacturer', models.CharField(max_length=200)),
                ('modelName', models.CharField(max_length=200)),
                ('releaseDate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]