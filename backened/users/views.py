from .models import User
from .serializers import UserModelSerializer
from rest_framework import viewsets
from rest_framework import mixins


class UserViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
