"""
杂项组件

(1) 版本号获取器
(2) 随机Token生成器
"""
import abc
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

class AbstractTokenGenerator(object, metaclass=abc.ABCMeta):
    """
    登录令牌生成器
    """

    @abc.abstractmethod
    def generate_token(self, user, **kwargs):
        """
        生成令牌
        :param user: 用户信息
        :param kwargs: 其他参数
        :return: 令牌
        """


class UUIDTokenGenerator(AbstractTokenGenerator):
    """
    UUID登录令牌生成器
    """
    uuid_len = 36

    def generate_token(self, user, **kwargs):
        if self.uuid_len == 36:
            return str(uuid.uuid4())
        elif self.uuid_len == 32:
            return str(uuid.uuid4()).replace('-', '')
        else:
            raise ValueError('uuid_len must be 32 or 36')


class RandomStrTokenGenerator(AbstractTokenGenerator):
    """
    随机字符串登录令牌生成器
    """
    random_str_length = 32

    def generate_token(self, user, **kwargs):
        return ''.join(random.choice(string.ascii_letters) for _ in range(self.random_str_length))
