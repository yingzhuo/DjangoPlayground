from django.http import HttpRequest
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from application.models import User
from common.api import CODE_OK


class CommonAuthenticator(BaseAuthentication):
    """
    通用权限验证器
    """

    def authenticate(self, request):
        if isinstance(request, HttpRequest):
            return None

        token = request.headers.get('Authorization', None)

        if not token:
            raise exceptions.AuthenticationFailed(code=CODE_OK, detail='令牌缺失')

        try:
            user = User.objects.filter(current_token=token)[0]
        except IndexError:
            user = None

        if not user:
            raise exceptions.AuthenticationFailed(code=CODE_OK, detail='令牌错误')

        return user, token
