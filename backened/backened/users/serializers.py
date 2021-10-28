from rest_framework.serializers import ModelSerializer
from users.models import CustomUser


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'firstname', 'lastname']


class V2UserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'is_superuser', 'is_staff', 'email', 'username', 'firstname', 'lastname']
