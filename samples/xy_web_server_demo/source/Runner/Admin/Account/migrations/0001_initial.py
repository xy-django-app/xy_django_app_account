# Generated by Django 5.1.2 on 2024-10-31 11:04

import xy_django_app_account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdminUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "date_of_birth",
                    models.DateTimeField(auto_now=True, verbose_name="生日"),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="是否启用"),
                ),
                (
                    "is_admin",
                    models.BooleanField(default=False, verbose_name="是否是管理员"),
                ),
                (
                    "email",
                    models.EmailField(max_length=255, unique=True, verbose_name="邮箱"),
                ),
                (
                    "username",
                    models.CharField(
                        default="", max_length=255, unique=True, verbose_name="用户名"
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        blank=True,
                        choices=[("man", "男"), ("female", "女"), ("unknown", "未知")],
                        default="man",
                        max_length=15,
                        verbose_name="性别",
                    ),
                ),
                (
                    "thumb",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=xy_django_app_account.models.user__thumbnails,
                        verbose_name="头像",
                    ),
                ),
                (
                    "age",
                    models.IntegerField(
                        blank=True, default=0, null=True, verbose_name="年龄"
                    ),
                ),
                (
                    "expires_time",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="登陆过期时间"
                    ),
                ),
                (
                    "nickname",
                    models.CharField(
                        blank=True, default="", max_length=255, verbose_name="昵称"
                    ),
                ),
                (
                    "userid",
                    models.CharField(
                        blank=True,
                        default="d112bbadd03436769f149ce731ee73e0",
                        max_length=100,
                        unique=True,
                        verbose_name="用户ID",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "用户",
                "verbose_name_plural": "用户",
            },
        ),
    ]