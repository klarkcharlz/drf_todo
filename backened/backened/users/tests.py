from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from backened.users.models import CustomUser
from backened.users.views import UserViewSet
from django.contrib.auth.models import User as SuperUser


class UserTestCase(APITestCase):

    def setUp(self):
        self.admin = SuperUser.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        self.client.login(username='admin', password='admin')

    def test_user_list(self):
        CustomUser.objects.create(username="test_name", firstname='Юзер', lastname='Юзерович', email='test@test.com')
        res = self.client.get('/api/users/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data['results']), 1)
        self.client.logout()
        res = self.client.get('/api/users/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_post(self):
        res = self.client.post('/api/users/', {
            'email': 'test@user.com',
            'username': 'testXxX',
            'firstname': 'Юзерслав',
            'lastname': 'Юзерович'
        })
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_factory(self):
        factory = APIRequestFactory()
        view = UserViewSet.as_view({'get': 'list'})
        request = factory.get('/api/users/')
        res = view(request)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        request = factory.get('/api/users/')
        force_authenticate(request, self.admin)
        res = view(request)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
