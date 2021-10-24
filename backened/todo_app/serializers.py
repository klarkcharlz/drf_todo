from rest_framework.serializers import ModelSerializer

from todo_app.models import Project, Todo
from users.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'url', 'users']


class TodoModelSerializer(ModelSerializer):
    project = ProjectModelSerializer()
    user = UserModelSerializer()

    class Meta:
        model = Todo
        fields = ['id', 'project', 'user', 'text', 'is_active', 'created_at', 'updated_at']


class TodoModelCreateSerializer(ModelSerializer):

    class Meta:
        model = Todo
        fields = ['project', 'user', 'text']


class ProjectModelCreateSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['name', 'url', 'users']
