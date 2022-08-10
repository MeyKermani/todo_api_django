from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class TYPE:
        DEVELOPER = 1
        PROJECT_MANAGER = 2

        choices = (
            (DEVELOPER, _('Developer')),
            (PROJECT_MANAGER, _('Project Manager')),
        )

    user_type = models.SmallIntegerField(choices=TYPE.choices, default=TYPE.DEVELOPER)

    def __str__(self):
        if self.is_staff:
            role_name = "Staff"
        else:
            role_name = "Developer" if self.user_type==1 else "Project Manager"
        return f"{role_name}::{self.get_full_name()}"
