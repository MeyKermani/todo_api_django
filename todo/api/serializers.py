from rest_framework import serializers
from todo.models import Task, Project
from users.api.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    project_manager_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Project
        fields = ["project_manager_name", "title", "description", "created_at"]

    def get_project_manager_name(self, obj):
        return obj.project_manager.get_full_name()


class TaskSerializer(serializers.ModelSerializer):
    assignees = UserSerializer(many=True, read_only=True)
    project_title = serializers.SerializerMethodField(read_only=True)
    task_title = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Task
        fields = ["pk", "project_title", "task_title", "description", "assignees", "done", "due_time"]

    def get_project_title(self, obj):
        return obj.project.title

    def get_task_title(self, obj):
        return obj.title




