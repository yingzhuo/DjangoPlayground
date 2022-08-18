"""
杂项组件

(1) 版本号获取器
"""
from rest_framework.versioning import URLPathVersioning


class Versioning(URLPathVersioning):
    """
    版本号获取器
    """

    version_param = 'version'
    default_version = 'v1'
    allowed_versions = ['v1', 'v2', 'v3', ]
