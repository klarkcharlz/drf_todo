from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from mixer.backend.django import mixer
from backened.todo_app.models import Project, Todo
from django.contrib.auth.models import User as SuperUser


class TestAuthorViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = SuperUser.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        self.client.login(username='admin', password='admin')

    def test_get_project(self):
        mixer.blend(Project)
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_todo(self):
        mixer.blend(Todo)
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    # def test_post_todo(self):
    #     user = mixer.blend(Project)
    #     project = mixer.blend(Project)
    #     res = self.client.post('/api/todo/', {
    #         'project': project.id,
    #         'user': user.id,
    #         'text': "Hello"})
    #     self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    #     todo = Todo.objects.get(id=res.data['results']['id'])
    #     self.assertEqual(todo.text, 'Hello')
