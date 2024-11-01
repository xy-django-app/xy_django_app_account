from django.utils.translation import gettext_lazy as _

# Create your models here.
from xy_django_app_account.abstracts import (
    AdminUserManager as xyAdminUserManager,
    MAAdminUser as xyAdminUser,
)


class MAdminUserManager(xyAdminUserManager):
    pass


class MAdminUser(xyAdminUser):
    objects = MAdminUserManager()

    class Meta:
        verbose_name = _("用户")
        verbose_name_plural = _("用户")
        app_label = "Account"
