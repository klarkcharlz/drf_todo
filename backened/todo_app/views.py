from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class PageLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectViewSet(mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    pagination_class = PageLimitOffsetPagination


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TodoViewSet(mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_fields = ['project']

    def destroy(self, request, pk=None):
        Todo.objects.filter(pk=pk).update(is_active=False)
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)
