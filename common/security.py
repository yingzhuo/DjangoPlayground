"""
鉴权相关组件
"""
from rest_framework.permissions import BasePermission
from rest_framework.throttling import BaseThrottle

from application.dao.user import UserDao
from application.models import User
from django_sugar.web import auth, token


class TokenBasedAuthenticator(auth.TokenBasedAuthenticator, token.HeaderTokenResolver, token.TokenBasedUserFinder):
    def get_user_by_token(self, current_token, **kwargs):
        return UserDao.find_by_current_token(current_token)


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
