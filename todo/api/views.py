from rest_framework import generics
from todo.api.serializers import ProjectSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated
from todo.api.permissions import IsTaskAssigneeOrProjectManager


class ProjectListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ProjectSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.order_by('-created_at')
    paginate_by = 100


class ProjectTaskListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = TaskSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.order_by('-updated_at')
    lookup_url_kwarg = "project_id"
    paginate_by = 100

    def get_queryset(self):
        project_id = self.kwargs.get(self.lookup_url_kwarg, None)
        queryset = self.queryset.filter(project_id=project_id)
        return queryset


class ProjectCurrentDeveloperTaskListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = TaskSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.order_by('-updated_at')
    lookup_url_kwarg = "project_id"
    paginate_by = 100

    def get_queryset(self):
        project_id = self.kwargs.get(self.lookup_url_kwarg, None)
        queryset = self.queryset.filter(
            project_id=project_id, assignees=self.request.user
        )
        return queryset


class TaskListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = TaskSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.order_by('-updated_at')
    paginate_by = 100


class TaskUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsTaskAssigneeOrProjectManager]
    serializer_class = TaskSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()
    lookup_field = 'pk'


class TaskDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsTaskAssigneeOrProjectManager]
    serializer_class = TaskSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()


