"""
用户相关模型及序列化器
"""

from django.db import models
from rest_framework import serializers

from application.models.gender import Gender


class UserToken(models.Model):
    """
    用户登录令牌
    """
    token_value = models.CharField(max_length=2000, null=True, db_column='token_value')
    created_datetime = models.DateTimeField(null=False, db_column='created_time')

    class Meta:
        db_table = 't_user_token'


class User(models.Model):
    """
    系统用户
    """
    username = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=32, null=False, blank=False)
    email = models.CharField(max_length=100, null=True)
    roles = models.CharField(max_length=200, null=True, db_column='role_list')
    gender = models.CharField(choices=Gender.choices(), max_length=10, null=True, db_column='sex')
    user_token = models.OneToOneField(UserToken, null=True, on_delete=models.CASCADE, db_constraint=False)
    dob = models.DateField(null=True, db_column='date_of_birth')

    @property
    def role_list(self):
        return map(str.strip, self.roles.split(','))

    class Meta:
        db_table = 't_user'


class UserSerializer(serializers.ModelSerializer):
    """
    用户类通用序列化器
    """
    # gender_value = serializers.IntegerField(source='get_gender_display')
    dob = serializers.DateField(format='%Y-%m-%d', required=False)
    role_list = serializers.ListField()

    class Meta:
        model = User
        exclude = ['password', 'roles', 'user_token']
        depth = 0
