from common.api import CODE_OK


class BusinessException(Exception):
    """
    业务异常
    """
    code = CODE_OK
    detail = None

    def __int__(self, *, code=None, detail=None):
        self.code = code or CODE_OK
        self.detail = detail or '(业务异常)'


# 登录失败
BE_LOGIN_FAILED = BusinessException(CODE_OK, '用户名或密码错误')
