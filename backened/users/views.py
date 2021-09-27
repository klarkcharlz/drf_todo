from rest_framework.generics import get_object_or_404
from .models import User
from .serializers import UserModelSerializer
from rest_framework.response import Response
from rest_framework import viewsets


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        User.objects.filter(pk=pk).update(**request.data)
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        User.objects.filter(pk=pk).update(**request.data)
        user = get_object_or_404(User, pk=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)
