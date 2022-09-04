r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
from django.db import models
from rest_framework import serializers


class FileMeta(models.Model):
    """
    文件元数据
    """

    path = models.CharField(max_length=2048, null=False, blank=False, db_column='path')
    created_date = models.DateTimeField(null=False, db_column='created_date')
    created_user_id = models.IntegerField(null=False, db_column='created_user_id')

    class Meta:
        db_table = 't_filemeta'


class FileMetaSerializer(serializers.ModelSerializer):
    """
    文件元数据相关序列化器
    """

    created_date = serializers.DateTimeField(format='%F %T')

    class Meta:
        model = FileMeta
        fields = [
            'id',
            'created_date',
        ]
