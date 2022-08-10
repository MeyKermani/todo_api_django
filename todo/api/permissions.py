from rest_framework import permissions
from users.models import User


class IsTaskAssigneeOrProjectManager(permissions.BasePermission):
    """
    Custom permission to only allow task assignee or project manager of a task to edit it.
    """

    def has_object_permission(self, request, view, obj):

        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the owner of object.
        if request.user.user_type == User.TYPE.PROJECT_MANAGER and obj.project.project_manager == request.user:
            return True
        return request.user in obj.assignees.all()