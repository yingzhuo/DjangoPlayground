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


# ----------------------------------------------------------------------------------------------------------------------

class UserWithToken(object):
    """
    简单模型，封装用户实体和令牌
    """
    user = None
    token = None

    def __init__(self, **kwargs):
        self.user = kwargs.get('user')
        self.token = kwargs.get('token')


class UserWithTokenSerializer(serializers.Serializer):
    """
    UserWithToken序列化器
    """

    id = serializers.IntegerField(source='user.id')
    username = serializers.CharField(source='user.username')
    role_list = serializers.ListField(source='user.role_list')
    token = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        pass

# ----------------------------------------------------------------------------------------------------------------------
