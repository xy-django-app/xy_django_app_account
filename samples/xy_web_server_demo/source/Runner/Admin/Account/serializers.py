# -*- coding: UTF-8 -*-
__author__ = "余洋"
__doc__ = "serializers"
"""
  * @File    :   serializers.py
  * @Time    :   2024/10/31 16:49:16
  * @Author  :   余洋
  * @Version :   0.0.1
  * @Contact :   yuyangit.0515@qq.com
  * @License :   (C)Copyright 2019-2024, 希洋 (Ship of Ocean)
  * @Desc    :   
"""

from django.contrib.auth import get_user_model

User = get_user_model()
from xy_django_app_account.serializers import SUser as xySUser, VSUser as xyVSUser


class SAdminUser(xySUser):

    class Meta:
        model = User
        fields = "__all__"


class VSUser(xyVSUser):
    queryset = User.objects.all()
    serializer_class = SAdminUser
