"""
杂项组件

(1) 版本号获取器
(2) 随机Token生成器
"""
import random
import string
import uuid

from rest_framework.versioning import URLPathVersioning


class Versioning(URLPathVersioning):
    """
    版本号获取器
    """

    version_param = 'version'
    default_version = 'v1'
    allowed_versions = ['v1', 'v2', 'v3', ]


# ----------------------------------------------------------------------------------------------------------------------

class TokenGenerator(object):
    """
    登录令牌生成器
    """

    def generate_token(self, user):
        raise TypeError('abstract method')


class UUIDTokenGenerator(TokenGenerator):
    """
    UUID登录令牌生成器
    """
    uuid_len = 36

    def generate_token(self, user):
        if self.uuid_len == 36:
            return str(uuid.uuid4())
        elif self.uuid_len == 32:
            return str(uuid.uuid4()).replace('-', '')
        else:
            pass


class RandomStrTokenGenerator(TokenGenerator):
    """
    随机字符串登录令牌生成器
    """
    random_str_length = 32

    def generate_token(self, user):
        return ''.join(random.choice(string.ascii_letters) for _ in range(self.random_str_length))
