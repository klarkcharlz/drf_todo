"""ToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from todo_app.views import ProjectViewSet, TodoViewSet, TodoViewSetCreate
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="ToDo",
        default_version='1.0',
        description="ToDo project",
        contact=openapi.Contact(email="admin@admin.admin"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

router = DefaultRouter()
router.register('users', UserViewSet, basename="users")
router.register('projects', ProjectViewSet, basename="projects")
router.register('todo', TodoViewSet, basename="todo")
router.register('create_todo', TodoViewSetCreate, basename="create_todo")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui()),

]
