# Generated by Django 4.1.7 on 2023-04-22 10:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='user_favorites',
            field=models.ManyToManyField(related_name='user_favorites', to=settings.AUTH_USER_MODEL, verbose_name='Избранные фотографии'),
        ),
    ]
