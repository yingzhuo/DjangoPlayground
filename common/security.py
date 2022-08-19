"""
鉴权相关组件
"""
import abc

from django.http import HttpRequest
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.throttling import BaseThrottle

from application.dao.user import UserDao
from application.models import User


class AbstractTokenResolver(object, metaclass=abc.ABCMeta):
    """
    令牌解析器
    """

    @abc.abstractmethod
    def resolve_token(self, request, **kwargs):
        """
        从请求中获取令牌
        :param request: 请求对象
        :param kwargs: 其他参数
        :return: 令牌字符串或None
        """


class HeaderTokenResolver(AbstractTokenResolver):
    header_name = 'Authorization'
    prefix = ''

    def resolve_token(self, request, **kwargs):
        header_value = request.headers.get(self.header_name, None)

        if header_value is None or not header_value.startswith(self.prefix):
            # 找不到此请求头或者值不以指定的前缀开始
            return None
        else:
            # 返回令牌字符串
            return header_value[len(self.prefix):]


# ----------------------------------------------------------------------------------------------------------------------


class TokenBasedAuthenticator(BaseAuthentication, HeaderTokenResolver):
    """
    通用权限验证器

    通过令牌找到用户对象
    """

    def authenticate(self, request):
        if isinstance(request, HttpRequest):
            return None

        # 尝试以反射的方式获取解析令牌的函数
        resolve_token = self.__getattribute__('resolve_token')

        if resolve_token is None:
            # 没有混入特质则无法进一步工作
            return None

        token = resolve_token(request)

        if not token:
            # 无法解析出令牌
            return None

        user = UserDao.find_by_current_token(token)

        if not user:
            raise exceptions.AuthenticationFailed()

        return user, token


# ----------------------------------------------------------------------------------------------------------------------


class RoleUser(BasePermission):
    """
    用户角色

    只要认证了，都赋予此角色
    """

    def has_permission(self, request, view):
        # 只要认证了，都赋予此角色
        return request.user is not None


class RoleVIP(BasePermission):
    """
    VIP角色
    """

    def has_permission(self, request, view):

        # ROOT > SVIP > VIP
        if RoleRoot().has_permission(request, view) or RoleSVIP().has_permission(request, view):
            return True

        user = request.user

        if not user or not isinstance(user, User):
            return False

        return 'ROLE_VIP' in user.role_list() or 'ROLE_SVIP' in user.role_list()


class RoleSVIP(BasePermission):
    """
    SVIP角色
    """

    def has_permission(self, request, view):
        # ROOT > SVIP
        if RoleRoot().has_permission(request, view):
            return True

        user = request.user

        if not user or not isinstance(user, User):
            return False

        return 'ROLE_SVIP' in user.role_list()


class RoleRoot(BasePermission):
    """
    ID等于1的用户为Root用户
    """

    def has_permission(self, request, view):
        user = request.user

        if not user or not isinstance(user, User):
            return False

        return user.id == 1


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
