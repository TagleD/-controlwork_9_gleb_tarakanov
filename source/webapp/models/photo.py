from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):
    image = models.ImageField(
        null=False,
        blank=False,
        upload_to='photos',
        verbose_name='Фотография',
    )
    caption = models.CharField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name='Подпись',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания",
    )
    author = models.ForeignKey(
        to=User,
        related_name='photos',
        verbose_name='Фотографии',
        null=False,
        on_delete=models.CASCADE,
    )
    user_favorites = models.ManyToManyField(
        verbose_name='Избранные фотографии',
        to=get_user_model(),
        related_name='user_favorites'
    )

    def __str__(self):
        return f'{self.author.username} - {self.caption}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
