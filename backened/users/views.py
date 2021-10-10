from users.models import CustomUser
from users.serializers import UserModelSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import DjangoModelPermissions


class UserViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
