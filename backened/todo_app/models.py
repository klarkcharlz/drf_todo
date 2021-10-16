from django.db import models
from users.models import CustomUser


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=64, verbose_name="Название")
    url = models.URLField(verbose_name="Ссылка на репозиторий", blank=True)
    users = models.ManyToManyField(CustomUser, verbose_name="Пользователи")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Проект", related_name='todo')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь", related_name='todo')
    text = models.CharField(max_length=255, verbose_name="Текст заметки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_active = models.BooleanField(default=True, verbose_name="Признак активного состояния заметки")

    def __str__(self):
        return f"{self.project}-{self.user}: {self.text[:20]}"

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"
