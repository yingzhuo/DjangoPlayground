from rest_framework.views import APIView

from application.models import User
from common import rand
from common.api import API, APIResponse
from common.business_exception import BE_LOGIN_FAILED


class LoginView(APIView):
    """
    处理登录请求
    """

    # 登录时不需要任何认证或授权
    authentication_classes = []

    def post(self, request, *args, **kwargs):

        username = request.GET.get('username', None)
        password = request.GET.get('password', None)

        if not username or not password:
            return APIResponse(API())

        user = User.objects.filter(username=username, password=password)[0]
        if not user:
            raise BE_LOGIN_FAILED

        token = rand.random_string()

        user.current_token = token
        user.save()

        api = API()
        api.add({
            'username': user.username,
            'token': token,
        })

        return APIResponse(api)
