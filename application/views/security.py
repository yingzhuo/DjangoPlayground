from rest_framework.views import APIView

from application.dao.user import UserManager
from common import rand
from common.api import API, APIResponse
from common.exception import BE_LOGIN_FAILED, BusinessException


class LoginView(APIView):
    """
    处理登录请求
    """

    # 登录时不需要任何认证或授权
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):

        username = request.GET.get('username', None)
        password = request.GET.get('password', None)

        if not username or not password:
            raise BusinessException(code=400, detail='参数缺失')

        user = UserManager.find_by_username_and_password(username, password)

        if not user:
            raise BE_LOGIN_FAILED

        user.current_token = rand.random_string()
        user.save()

        api = API(
            username=username,
            token=user.current_token,
        )

        return APIResponse(api)


class TokenInfoView(APIView):
    """
    检查Token信息

    简单返回当前用户名和令牌字符串
    """

    def get(self, request, *args, **kwargs):
        user = request.user
        token = request.auth

        api = API(
            username=user.username,
            token=token,
        )
        return APIResponse(api)
