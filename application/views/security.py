import json

from django.http import HttpResponse
from django.utils import timezone
from rest_framework.views import APIView

from application.dao.user import UserDao
from application.form.security import LoginFormSerializer
from application.models import UserToken
from application.views.security_vo import UserWithTokenSerializer, UserWithToken
from common.exception import BE_LOGIN_FAILED
from common.misc import UUIDTokenGenerator


class LoginView(APIView, UUIDTokenGenerator):
    """
    处理登录请求

    URL: /v1/security/login/
    """

    # 登录时不需要任何认证
    authentication_classes = []

    # 登录时不需要任何授权
    permission_classes = []

    def post(self, request, *args, **kwargs):

        client_data = {
            **request.GET,
            **request.data,
        }

        ser = LoginFormSerializer(data=client_data)
        ser.is_valid(raise_exception=True)
        username = ser.validated_data['username']
        password = ser.validated_data['password']

        user = UserDao.find_by_username_and_password(username, password)

        if user is None:
            raise BE_LOGIN_FAILED

        new_token = self.generate_token(user)

        # 更新持久化的令牌
        if user.user_token is None:
            # 第一次登录
            user_token = UserToken(token_value=new_token, created_datetime=timezone.now())
        else:
            # 非第一登录
            user_token = user.user_token
            user_token.token_value = new_token
            user_token.created_datetime = timezone.now()

        user_token.save()
        user.user_token = user_token
        user.save()

        uts = UserWithTokenSerializer(instance=UserWithToken(user=user, token=new_token))
        ret = json.dumps(uts.data, ensure_ascii=False)
        return HttpResponse(ret, content_type='application/json; charset=utf-8')


class TokenInfoView(APIView):
    """
    检查Token信息

    简单返回当前用户名和令牌字符串

    URL: /v1/security/token/
    """

    def get(self, request, *args, **kwargs):
        user = request.user
        token = request.auth
        version = request.version

        ret = json.dumps(
            {
                'username': user.username,
                'token': token,
                'api_version': version,
            },
            ensure_ascii=False,
        )
        return HttpResponse(ret, content_type='application/json; charset=utf-8')
