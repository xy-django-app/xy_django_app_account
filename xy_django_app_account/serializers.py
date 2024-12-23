# -*- coding: UTF-8 -*-

from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework import viewsets
from collections import OrderedDict
from collections.abc import Mapping
from rest_framework.relations import PKOnlyObject
from rest_framework.fields import (
    SkipField,
)
from xy_django_serializer.serializers import Serializer


# Serializers define the API representation.
class SUser(Serializer):
    default_value = ""

    class Meta:
        abstract = True
        model = User
        fields = "__all__"

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = OrderedDict()
        fields = self._readable_fields

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            # We skip `to_representation` for `None` values so that fields do
            # not have to explicitly deal with that case.
            #
            # For related fields with `use_pk_only_optimization` we need to
            # resolve the pk value.
            check_for_none = (
                attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            )
            if check_for_none is None:
                ret[field.field_name] = ""
            else:
                ret[field.field_name] = field.to_representation(attribute)

        return ret


# ViewSets define the view behavior.
class VSUser(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SUser
