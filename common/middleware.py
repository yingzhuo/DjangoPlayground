"""
中间件
"""
from django.utils.deprecation import MiddlewareMixin

from common.http import HttpRequestDescriptor


class LoggingMiddleware(MiddlewareMixin):
    """
    抽象请求日志记录中间件
    """

    def process_request(self, request):
        if self.__getattribute__('do_log'):
            do_log = self.__getattribute__('do_log')
            do_log(HttpRequestDescriptor(request))

        return self.get_response(request)


# ----------------------------------------------------------------------------------------------------------------------

class StdoutLoggingMixin(object):
    """
    标准控制台请求日志特质
    """

    def do_log(self, request_descriptor):

        if request_descriptor is None:
            return

        if not isinstance(request_descriptor, HttpRequestDescriptor):
            raise TypeError('wrong type')

        print('-' * 120)
        print(request_descriptor)
        print('-' * 120)


class StdoutLoggingMiddleware(LoggingMiddleware, StdoutLoggingMixin):
    """
    请求日志记录中间件

    此中间件输出日志到标准控制台
    """
    pass
