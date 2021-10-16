from users.models import CustomUser
from users.serializers import UserModelSerializer, V2UserModelSerializer
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import DjangoModelPermissions


class UserViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return V2UserModelSerializer
        return UserModelSerializer
