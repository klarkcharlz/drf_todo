from todo_app.models import Project, Todo
from todo_app.serializers import ProjectModelSerializer, TodoModelSerializer, \
    TodoModelCreateSerializer, ProjectModelCreateSerializer
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from django_filters import rest_framework as filters
import django_filters
from rest_framework import viewsets, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import mixins
from django.db import models as django_models
from rest_framework.permissions import DjangoModelPermissions


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class PageLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectViewSet(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [DjangoModelPermissions]
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


class TodoViewSet(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [DjangoModelPermissions]
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filter_class = TodoFilter

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("DELETE")
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class TodoViewSetCreate(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelCreateSerializer
    permission_classes = [DjangoModelPermissions]


class ProjectViewSetCreate(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                           viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelCreateSerializer
    permission_classes = [DjangoModelPermissions]
