from rest_framework.serializers import ModelSerializer
from users.models import CustomUser


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'firstname', 'lastname']
