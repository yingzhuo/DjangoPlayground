r"""
 ____  _                           ____
|  _ \(_) __ _ _ __   __ _  ___   / ___| _   _  __ _  __ _ _ __
| | | | |/ _` | '_ \ / _` |/ _ \  \___ \| | | |/ _` |/ _` | '__|
| |_| | | (_| | | | | (_| | (_) |  ___) | |_| | (_| | (_| | |
|____// |\__,_|_| |_|\__, |\___/  |____/ \__,_|\__, |\__,_|_|
    |__/             |___/                     |___/

    https://github.com/yingzhuo/django-sugar

"""
from django_sugar import valueobject
from rest_framework import serializers


class UsernameMixin(serializers.Serializer):
    username = serializers.CharField(
        error_messages={
            'required': '用户名不可为空',
            'min_length': '用户名长度必须在2到12之间',
            'max_length': '用户名长度必须在2到12之间',
        },
        required=True,
        min_length=2,
        max_length=12,
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class PasswordMixin(serializers.Serializer):
    password = valueobject.PasswordField(
        error_messages={
            'invalid': '密码非法',
            'min_length': '密码长度必须在6到16之间',
            'max_length': '密码长度必须在2到16之间',
        },
        required=True,
        min_length=6,
        max_length=16,
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
