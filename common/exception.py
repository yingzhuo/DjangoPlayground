r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
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
