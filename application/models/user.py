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
    gender = models.CharField(choices=Gender.choices(), max_length=10, null=True, db_column='sex')
    current_token = models.CharField(max_length=36, null=True, db_column='login_token')
    dob = models.DateField(null=True, db_column='date_of_birth')

    @property
    def role_list(self):
        return map(str.strip, self.roles.split(','))

    class Meta:
        db_table = 't_user'


# ----------------------------------------------------------------------------------------------------------------------

class UserSerializer(serializers.ModelSerializer):
    role_list = serializers.ListField()
    dob = serializers.DateField(format='%Y-%m-%d', required=False)
    gender_value = serializers.IntegerField(source='get_gender_display')

    class Meta:
        model = User
        exclude = ['password', 'current_token', 'roles']
