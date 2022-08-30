r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
from datetime import datetime, timezone, timedelta
from typing import Optional, Dict, Any

from django_sugar.web import http, token_jwt, pwdencoder
from rest_framework.response import Response
from rest_framework.views import APIView

from application.dao.user import UserDao
from application.form.security import LoginFormSerializer
from application.views.security_vo import UserWithTokenSerializer, UserWithToken
from common.constants import JWT_SECRET_KEY
from common.exception import BE_LOGIN_FAILED


class LoginView(APIView, token_jwt.HS256JWTTokenGenerator, pwdencoder.CompositePasswordEncoder):
    """
    处理登录请求

    URL: /v1/security/login/
    """

    # 登录时不需要任何认证或授权
    authentication_classes = []
    permission_classes = []

    # 生成UUID时生成32位长度的
    remove_uuid_hyphen = True

    # JWT加密key
    hs256_secret = JWT_SECRET_KEY

    def post(self, request, *args, **kwargs):
        client_data = http.get_client_sent_data(request)

        ser = LoginFormSerializer(data=client_data)
        ser.is_valid(raise_exception=True)
        username = ser.validated_data['username']
        raw_pass = ser.validated_data['password']

        user = UserDao.find_by_username(username)

        if user is None:
            raise BE_LOGIN_FAILED

        if not self.password_matches(raw_pass, user.password):
            raise BE_LOGIN_FAILED

        jwt_token = self.generate_token(user)

        uts = UserWithTokenSerializer(instance=UserWithToken(user=user, token=jwt_token))
        return Response(data=uts.data)

    def user_to_jwt_payload(self, user) -> Optional[Dict[str, Any]]:
        return {
            'id': user.id,
            'username': user.username,
            'roles': user.roles,
            'exp': datetime.now(tz=timezone.utc) + timedelta(days=1),
            'nbf': datetime.now(tz=timezone.utc),
        }


class TokenInfoView(APIView):
    """
    检查Token信息

    简单返回当前用户名和令牌字符串

    URL: /v1/security/token/
    """

    def get(self, request, *args, **kwargs):
        user = request.user
        tk = request.auth
        version = request.version

        ret = {
            'username': user['username'],
            'token': tk,
            'api_version': version,
        }
        return Response(data=ret)
