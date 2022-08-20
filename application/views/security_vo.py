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
