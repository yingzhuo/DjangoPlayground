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


class CommonFileUploadForm(serializers.Serializer):

    # 文件名
    filename = serializers.CharField(
        error_messages={
            'required': '文件名缺失',
            'blank': '文件名缺失',
        },
        required=True,
        allow_blank=False,
    )

    file_data = serializers.FileField(
        error_messages={
            'required': '文件缺失',
        },
        required=True,
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
