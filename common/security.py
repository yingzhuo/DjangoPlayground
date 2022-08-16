from rest_framework.authentication import BaseAuthentication


class CommonAuthenticator(BaseAuthentication):
    """
    通用权限验证器
    """

    def authenticate(self, request):
        # TODO: JWT实现
        return None
