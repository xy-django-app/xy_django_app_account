<!--
 * @Author: 余洋 yuyangit.0515@qq.com
 * @Date: 2024-10-18 13:02:22
 * @LastEditors: 余洋 yuyangit.0515@qq.com
 * @LastEditTime: 2024-10-23 20:52:22
 * @FilePath: /xy_django_app_account/readme/README.en.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# xy_django_app_account

| [简体中文](../README.md)         | [繁體中文](./README.zh-hant.md)        |                      [English](./README.en.md)          |
| ----------- | -------------|---------------------------------------|

## Description

Backend account data model.

## Source Code Repositories

| [Github](https://github.com/xy-django-app/xy_django_app_account.git)         | [Gitee](https://gitee.com/xy-opensource/xy_django_app_account.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_django_app_account.git)          |
| ----------- | -------------|---------------------------------------|

## Installation

```bash
# bash
pip install xy_django_app_account
```

## How to use

##### 1. Direct import

- ###### 1. Set global configuration

Add the following configuration to the [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py) file in the Django project
```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "xy_django_app_account",
    "Demo",
    "Resource",
    "Media",
]

AUTH_USER_MODEL = "xy_django_app_account.AdminUser"
# 启动工程后访问 http://127.0.0.1:8401/admin 验证账户系统
```

- ###### 2. Run project

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证账户管理系统
```

##### 2. Customize

- ###### 1. Create Account module

> Operation [Sample Project](../samples/xy_web_server_demo/)

```bash
# bash
xy_web_server -w django startapp Account
# Account 模块创建在 source/Runner/Admin/Account 
```

- ###### 2. Set global configuration

Add the following configuration to the settings.py file in the Django project
For example: [settings.py](../samples/xy_web_server_demo/source/Runner/Admin/xy_web_server_demo/settings.py)

```python
# settings.py

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Demo",
    "Resource",
    "Media",
    "Account",
]

AUTH_USER_MODEL = "Account.AdminUser"
# 启动工程后访问 http://127.0.0.1:8401/admin 验证账户系统
```

- ###### 3. Add the following code to the [models.py](../samples/xy_web_server_demo/source/Runner/Admin/Account/models.py) file of the [Account](../samples/xy_web_server_demo/source/Runner/Admin/Account) module

```python
# models.py
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

```

- ###### 4. Add the following code to the [admin.py](../samples/xy_web_server_demo/source/Runner/Admin/Account/admin.py) file of the [Account](../samples/xy_web_server_demo/source/Runner/Admin/Account) module

```python
# admin.py
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

```

- ###### 5. Run project

```bash
xy_web_server -w django makemigrations
xy_web_server -w django migrate
# 同步数据表
xy_web_server -w django start
# 启动工程后访问 http://127.0.0.1:8401/admin 验证账户管理系统
```


##### Run [Sample Project](../samples/xy_web_server_demo)

> For detailed usage of the sample project, please go to the following repository <b style="color: blue">xy_web_server.git</b> 

| [Github](https://github.com/xy-web-service/xy_web_server.git)         | [Gitee](https://gitee.com/xy-opensource/xy_web_server.git)        |                      [GitCode](https://gitcode.com/xy-opensource/xy_web_server.git)          |
| ----------- | -------------|---------------------------------------| 

## License
xy_django_app_account is licensed under the <Mulan Permissive Software License，Version 2>. See the [LICENSE](../LICENSE) file for more info.

## Donate

If you think these tools are pretty good, Can you please have a cup of coffee?  

![pay-total](./pay-total.png)  


## Contact

```
WeChat: yuyangiit
Mail: yuyangit.0515@qq.com
```