from rest_framework.serializers import ModelSerializer, StringRelatedField

from .models import Project, Todo
from users.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)
    # users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['name', 'url', 'users']


class TodoModelSerializer(ModelSerializer):
    project = ProjectModelSerializer()
    user = UserModelSerializer()

    class Meta:
        model = Todo
        fields = ['project', 'user', 'text', 'is_active']
