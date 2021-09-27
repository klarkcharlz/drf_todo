from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.pagination import LimitOffsetPagination


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class PageLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectViewSet(viewsets.ViewSet):
    filterset_class = ProjectFilter
    pagination_class = PageLimitOffsetPagination

    def list(self, request):
        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializer(project)
        return Response(serializer.data)

    def update(self, request, pk=None):
        Project.objects.filter(pk=pk).update(**request.data)
        user = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializer(user)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        Project.objects.filter(pk=pk).update(**request.data)
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectModelSerializer(project)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        Project.objects.filter(pk=pk).delete()
        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects, many=True)
        return Response(serializer.data)

    def create(self, request):
        Project(**request.data).save()
        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects, many=True)
        return Response(serializer.data)


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoViewSet(viewsets.ViewSet):
    pagination_class = TodoLimitOffsetPagination
    filterset_fields = ['project']

    def list(self, request):
        todos = Todo.objects.all()
        serializer = TodoModelSerializer(todos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        todos = get_object_or_404(Todo, pk=pk)
        serializer = TodoModelSerializer(todos)
        return Response(serializer.data)

    def update(self, request, pk=None):
        Todo.objects.filter(pk=pk).update(**request.data)
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        Todo.objects.filter(pk=pk).update(**request.data)
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        Todo.objects.filter(pk=pk).update(is_active=False)
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)

    def create(self, request):
        Todo(**request.data).save()
        todos = Todo.objects.all()
        serializer = TodoModelSerializer(todos, many=True)
        return Response(serializer.data)
