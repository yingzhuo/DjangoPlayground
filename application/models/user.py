"""
用户相关模型及序列化器
"""
from django.db import models
from rest_framework import serializers

from application.models.gender import Gender


class User(models.Model):
    """
    用户
    """
    username = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=32, null=False, blank=False)
    email = models.CharField(max_length=100, null=True)
    roles = models.CharField(max_length=200, null=True, db_column='role_list')
    current_token = models.CharField(max_length=36, null=True, db_column='login_token')
    gender = models.IntegerField(choices=Gender.choices(), null=True, db_column='sex')

    @property
    def role_list(self):
        return map(str.strip, self.roles.split(','))

    class Meta:
        db_table = 't_user'


# ----------------------------------------------------------------------------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    role_list = serializers.ListField()
    sex = serializers.CharField(source='get_gender_display')

    class Meta:
        model = User
        exclude = ['password', 'current_token', 'roles', 'gender']
