"""
用户相关模型及序列化器
"""

from django.db import models
from rest_framework import serializers

from application.models.gender import Gender


class User(models.Model):
    """
    系统用户
    """
    username = models.CharField(max_length=20, null=False, blank=False, unique=True)
    password = models.CharField(max_length=2048, null=False, blank=False)
    email = models.CharField(max_length=100, null=True)
    roles = models.CharField(max_length=200, null=True, db_column='role_list')
    gender = models.CharField(choices=Gender.choices(), max_length=10, null=True, db_column='sex')
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
        exclude = ['password', 'roles', ]
        depth = 0
