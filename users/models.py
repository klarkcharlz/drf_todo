from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
