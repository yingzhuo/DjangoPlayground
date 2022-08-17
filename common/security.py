"""
鉴权相关
"""
from django.http import HttpRequest
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission

from application.dao.user import UserDao
from application.models import User


class CommonAuthenticator(BaseAuthentication):
    """
    通用权限验证器
    """

    def authenticate(self, request):
        if isinstance(request, HttpRequest):
            return None

        token = request.headers.get('Authorization', None)

        if not token:
            raise exceptions.AuthenticationFailed()

        user = UserDao.find_by_current_token(token)

        if not user:
            raise exceptions.AuthenticationFailed()

        return user, token


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
        user = request.user

        if not user or not isinstance(user, User):
            return False

        return 'ROLE_VIP' in user.role_list()


class RoleSVIP(BasePermission):
    """
    SVIP角色
    """

    def has_permission(self, request, view):
        user = request.user

        if not user or not isinstance(user, User):
            return False

        return 'ROLE_SVIP' in user.role_list()
