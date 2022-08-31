"""
鉴权相关组件
"""
from django_sugar.web import auth, token_jwt
from rest_framework.permissions import BasePermission
from rest_framework.throttling import BaseThrottle

from common.constants import JWT_SECRET_KEY


class TokenBasedAuthenticator(auth.TokenBasedAuthenticator,
                              token_jwt.JwtTokenParser,
                              token_jwt.JwtTokenBasedUserFinder):
    # JWT加密key
    jwt_algorithm_and_key = JWT_SECRET_KEY

    def convert_user(self, user_dict):
        return user_dict


# ----------------------------------------------------------------------------------------------------------------------


class RoleUser(BasePermission):
    """
    用户角色

    只要认证了，都赋予此角色
    """

    def has_permission(self, request, view):
        # 只要认证了，都赋予此角色
        return request.user is not None


# ----------------------------------------------------------------------------------------------------------------------

class NullThrottle(BaseThrottle):
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
