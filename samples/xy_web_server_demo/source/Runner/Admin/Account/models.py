from django.utils.translation import gettext_lazy as _

# Create your models here.
from xy_django_app_account.models import (
    AdminUserManager as xyAdminUserManager,
    AdminUser as xyAdminUser,
)


class AdminUserManager(xyAdminUserManager):
    pass


class AdminUser(xyAdminUser):
    objects = AdminUserManager()

    class Meta:
        verbose_name = _("用户")
        verbose_name_plural = _("用户")
        app_label = "Account"
