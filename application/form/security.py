from rest_framework import serializers


class LoginFormSerializer(serializers.Serializer):
    """
    登录上行数据序列化器
    """

    username = serializers.CharField(
        error_messages={
            'required': '用户名不可为空'
        },
        validators=[],
    )

    password = serializers.CharField(
        error_messages={
            'required': '密码不可为空'
        },
    )
