from django.db import models


class User(models.Model):
    """
    用户
    """
    username = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=32, null=False, blank=False)
    email = models.CharField(max_length=100, null=True)
    current_token = models.CharField(max_length=36, null=True, db_column='login_token')

    class Meta:
        db_table = 't_user'
