from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django_filters import rest_framework as filters
import django_filters
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins
from django.db import models as django_models


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


class TodoFilter(filters.FilterSet):
    class Meta:
        model = Todo
        fields = {
            'created_at': ('lte', 'gte')
        }

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': django_filters.IsoDateTimeFilter
        },
    }


class TodoViewSet(mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filter_class = TodoFilter
    filterset_fields = ['project']

    def destroy(self, request, pk=None):
        Todo.objects.filter(pk=pk).update(is_active=False)
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)
