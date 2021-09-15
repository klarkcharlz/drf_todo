from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True, verbose_name="Электроная почта")
    username = models.CharField(max_length=64, verbose_name="Ник")
    firstname = models.CharField(max_length=64, verbose_name="Имя")
    lastname = models.CharField(max_length=64, verbose_name="Фамилия")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
