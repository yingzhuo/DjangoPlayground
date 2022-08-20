"""
业务异常及全局异常处理模块
"""
from rest_framework import exceptions, views


class BusinessException(exceptions.APIException):
    """
    业务异常
    """
    status_code = 400

    def __init__(self, *, status_code=None, detail=None):
        self.status_code = status_code or 400
        self.detail = detail or '(业务异常)'


# 登录失败
BE_LOGIN_FAILED = BusinessException(detail='用户名或密码错误')


# ----------------------------------------------------------------------------------------------------------------------

def custom_exception_handler(exc, context):
    # view = context.get('view')
    # args = context.get('args')
    # kwargs = context.get('kwargs')
    # request = context.get('request')
    return views.exception_handler(exc, context)
