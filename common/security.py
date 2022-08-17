"""
鉴权相关
"""
from django.http import HttpRequest
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from application.dao.user import UserManager


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

        user = UserManager.find_by_current_token(token)

        if not user:
            raise exceptions.AuthenticationFailed()

        return user, token


class RoleUser(object):
    """
    用户角色
    """

    def has_permission(self, request, view):
        # 只要认证了，都赋予此角色
        return request.user is not None
