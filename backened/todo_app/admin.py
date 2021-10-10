from django.contrib import admin
from todo_app.models import Project, Todo

# Register your models here.
admin.site.register(Project)
admin.site.register(Todo)