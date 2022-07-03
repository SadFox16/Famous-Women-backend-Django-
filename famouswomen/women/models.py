from django.contrib.auth.models import User
from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Ф.И.О')
    content = models.TextField(blank=True, verbose_name='Краткая биография')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория', related_name='womens')
    user = models.ForeignKey(User, verbose_name='Кем добавлена', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Женщина"
        verbose_name_plural = "Женщины"


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
