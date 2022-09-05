r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
from django_sugar.web import http
from rest_framework import versioning


class Versioning(versioning.URLPathVersioning):
    """
    版本号获取器
    """

    version_param = 'version'
    default_version = 'v1'
    allowed_versions = ['v1', 'v2', 'v3', ]


def bind_request_data(request, serializer_classes, *, squeeze=True, default_values: dict = None, **kwargs):
    """
    绑定请求数据

    :param request: 请求对象
    :param serializer_classes: 序列化器类型
    :param squeeze: 当结果value包含多个值时，是否只去最后一个值
    :param default_values: 可以设置一些缺省值
    :param kwargs: 其他参数
    :return: 合并后的数据(字典)
    """

    data = http.merge_client_data(request, squeeze=squeeze, default_values=default_values, **kwargs)
    serializer = serializer_classes(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.validated_data
