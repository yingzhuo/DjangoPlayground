r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
from rest_framework import serializers


class LoginFormSerializer(serializers.Serializer):
    """
    登录上行数据序列化器
    """

    username = serializers.CharField(
        error_messages={
            'required': '用户名不可为空',
            'min_length': '长度必须在2到12之间',
            'max_length': '长度必须在2到12之间',
        },
        validators=[],
        required=True,
        min_length=2,
        max_length=12,
    )

    password = serializers.CharField(
        error_messages={
            'required': '密码不可为空',
            'min_length': '长度必须在6到16之间',
            'max_length': '长度必须在6到16之间',
        },
        validators=[],
        required=True,
        min_length=6,
        max_length=16,
    )

    def validate_password(self, password_value):
        return password_value

    def update(self, instance, validated_data):
        # nop
        return instance

    def create(self, validated_data):
        # nop
        return None
