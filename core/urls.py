"""core URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.api.urls', namespace='users')),
    path('api/todo/', include('todo.api.urls', namespace='todo'))
]
