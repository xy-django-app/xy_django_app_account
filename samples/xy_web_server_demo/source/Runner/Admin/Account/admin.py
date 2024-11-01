from django.contrib import admin

# Register your models here.
from .models import MAdminUser
from xy_django_app_account.aabstracts import *


class AUserCreationForm(AAUserCreationForm):

    class Meta:
        model = MAdminUser
        fields = ("username",)


class AUserChangeForm(AAUserChangeForm):

    class Meta:
        model = MAdminUser
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


@admin.register(MAdminUser)
class AAdminUserAdmin(AAAdminUserAdmin):
    # The forms to add and change user instances
    form = AAUserChangeForm
    add_form = AAUserCreationForm
