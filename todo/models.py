from django.db import models
from users.models import User


class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    project_manager = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        null=True,
        limit_choices_to={'id__in': User.objects.filter(user_type=User.TYPE.PROJECT_MANAGER)}
    )

    def __str__(self):
        return f"Project::{self.title}"


class Task(models.Model):
    assignees = models.ManyToManyField(
        User,
        limit_choices_to={
            'id__in': User.objects.filter(user_type=User.TYPE.DEVELOPER)
        }
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_time = models.DateTimeField(null=True)
    title = models.CharField(max_length=256)
    description = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"Task::{self.title} from {self.project}"
