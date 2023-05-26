# Generated by Django 3.2 on 2023-05-25 04:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audiorecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Уникальный UUID')),
                ('audio', models.FileField(upload_to='downloads', verbose_name='Айдиофайл')),
            ],
        ),
    ]
