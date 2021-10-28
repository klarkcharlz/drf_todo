import json
import os

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from backened.users.models import User as AbstractUser

JSON_PATH = 'users/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('users')
        for user in users:
            print(user)
            new_user = AbstractUser(**user)
            new_user.save()

        # Создаем суперпользователя при помощи менеджера модели
        User.objects.create_superuser('django_drf', 'django_drf@geekshop.ru', 'django_drf')
