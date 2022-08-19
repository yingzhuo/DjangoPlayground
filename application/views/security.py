from django.http import HttpResponse
from django.utils import timezone
from rest_framework.views import APIView

from application.dao.user import UserDao
from application.form.security import LoginFormSerializer
from application.models import UserToken
from common.api import API, APIResponse
from common.exception import BE_LOGIN_FAILED, BusinessException
from common.misc import UUIDTokenGenerator


class LoginView(APIView, UUIDTokenGenerator):
    """
    处理登录请求

    URL: /v1/security/login
    """

    # 登录时不需要任何认证或授权
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):

        ser = LoginFormSerializer(data=request.data)
        if ser.is_valid(raise_exception=True):
            username = ser.validated_data['username']
            password = ser.validated_data['password']
        else:
            # TODO: 研究如何实现
            return HttpResponse('NG')

        # username = request.GET.get('username', None)
        # password = request.GET.get('password', None)

        if not username or not password:
            raise BusinessException(code=400, detail='参数缺失')

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

        api = API(
            username=username,
            token=new_token,
        )

        return APIResponse(api)


class TokenInfoView(APIView):
    """
    检查Token信息

    简单返回当前用户名和令牌字符串

    URL: /v1/security/token
    """

    def get(self, request, *args, **kwargs):
        user = request.user
        token = request.auth
        version = request.version

        api = API(
            username=user.username,
            token=token,
            api_version=version,
        )
        return APIResponse(api)
