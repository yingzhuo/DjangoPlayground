"""
业务异常及全局异常处理模块
"""
from django.http import Http404
from rest_framework import exceptions
from rest_framework.exceptions import PermissionDenied

from common.api import *


class BusinessException(exceptions.APIException):
    """
    业务异常
    """
    code = CODE_OK
    detail = None

    def __init__(self, *, code=None, detail=None):
        self.code = code or CODE_OK
        self.detail = detail or '(业务异常)'


# 登录失败
BE_LOGIN_FAILED = BusinessException(detail='用户名或密码错误')


# ----------------------------------------------------------------------------------------------------------------------

def custom_exception_handler(ex, context):
    api = API()

    if isinstance(ex, (Http404, exceptions.NotFound)):
        api.code = '404'
        api.error = '请求的资源未找到'

    elif isinstance(ex, exceptions.ValidationError):
        api.code = '400'
        api.error = '参数错误'

    elif isinstance(ex, exceptions.AuthenticationFailed):
        api.code = '401'
        api.error = '认证错误'

    elif isinstance(ex, (PermissionDenied, exceptions.PermissionDenied, exceptions.NotAuthenticated)):
        api.code = '403'
        api.error = '请求被决绝'

    elif isinstance(ex, exceptions.MethodNotAllowed):
        api.code = '405'
        api.error = '方法不支持'

    elif isinstance(ex, exceptions.NotAcceptable):
        api.code = '406'
        api.error = '应答格式不支持'

    elif isinstance(ex, exceptions.UnsupportedMediaType):
        api.code = '415'
        api.error = '不支持的媒体类型'

    elif isinstance(ex, exceptions.Throttled):
        api.code = '429'
        api.error = '请求次数过多'

    elif isinstance(ex, BusinessException):
        api.code = ex.code
        api.error = ex.detail

    else:
        api.code = CODE_SERVER_ERROR
        api.error = '服务器内部错误'

    return APIResponse(api, status=200)
