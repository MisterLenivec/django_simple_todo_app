from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(blank=True, verbose_name="Описание")
    complete = models.BooleanField(default=False, verbose_name="Завершен")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлен")

    def __str__(self):
        return self.title
