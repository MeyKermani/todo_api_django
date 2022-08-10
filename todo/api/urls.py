"""todoAPI URL Configuration
"""
from django.urls import path
from todo.api.views import ProjectListView, ProjectTaskListView, TaskListView, TaskUpdateView, TaskDeleteView,\
    ProjectCurrentDeveloperTaskListView
app_name = 'todo'
urlpatterns = [
    path('projects/', ProjectListView.as_view(), name="project_list"),
    path('project/<int:project_id>/tasks/', ProjectTaskListView.as_view(), name="project_task_list"),
    path('project/<int:project_id>/mytasks/',
         ProjectCurrentDeveloperTaskListView.as_view(),
         name="project_current_developer_task_list"
         ),
    path('tasks/', TaskListView.as_view(), name="task_list"),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name="task_update"),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name="task_update")
]