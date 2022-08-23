"""
杂项组件

(1) 版本号获取器
(2) 随机Token生成器
"""

from rest_framework import versioning


class Versioning(versioning.URLPathVersioning):
    """
    版本号获取器
    """

    version_param = 'version'
    default_version = 'v1'
    allowed_versions = ['v1', 'v2', 'v3', ]
