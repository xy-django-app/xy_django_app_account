from django.contrib import admin

# Register your models here.
from .models import AdminUser
from xy_django_app_account.admin import UserCreationForm as xyUserCreationForm
from xy_django_app_account.admin import UserChangeForm as xyUserChangeForm
from xy_django_app_account.admin import AdminUserAdmin as xyAdminUserAdmin


class UserCreationForm(xyUserCreationForm):

    class Meta:
        model = AdminUser
        fields = ("username",)


class UserChangeForm(xyUserChangeForm):

    class Meta:
        model = AdminUser
        fields = (
            "password",
            "email",
            "username",
            "is_active",
            "is_admin",
            "sex",
            "thumb",
            "age",
            "userid",
        )


@admin.register(AdminUser)
class AdminUserAdmin(xyAdminUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
