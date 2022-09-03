r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
from pathlib import Path

from django_sugar import web, lang
from rest_framework import permissions, throttling

JWT_SECRET_KEY = web.create_es256k_algorithm(
    public_key=lang.read_file_as_bytes(Path(__file__).parent / 'rsa.public'),
    private_key=lang.read_file_as_bytes(Path(__file__).parent / 'rsa.private'),
)


# ----------------------------------------------------------------------------------------------------------------------


class TokenBasedAuthenticator(web.TokenBasedAuthenticator,
                              web.CompositeTokenResolver,
                              web.JwtTokenBasedUserFinder):
    # JWT加密key
    jwt_algorithm_and_key = JWT_SECRET_KEY

    @staticmethod
    def convert_user(user_dict):
        # 可以从用户字典转换到其他实体
        return user_dict


# ----------------------------------------------------------------------------------------------------------------------


class RoleUser(permissions.BasePermission):
    """
    用户角色

    只要认证了，都赋予此角色
    """

    def has_permission(self, request, view):
        # 只要认证了，都赋予此角色
        return request.user is not None


# ----------------------------------------------------------------------------------------------------------------------

class NullThrottle(throttling.BaseThrottle):
    """
    请求限流器

    本项目不启用限流功能
    """

    def allow_request(self, request, view):
        return True

    def get_ident(self, request):
        """
        用户ID作为缓存的key
        :param request: 请求对象
        :return: 用户ID
        """
        return str(request.user.id)
