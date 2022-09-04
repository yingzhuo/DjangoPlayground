r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
from django.http import HttpResponse
from django.utils import deprecation
from django_sugar import web
from rest_framework import status


class SpiderDenyingMiddleware(deprecation.MiddlewareMixin):
    """
    拒绝蜘蛛用的Middleware
    """

    def process_request(self, request):
        maybe_spider = web.maybe_spider(request)
        if maybe_spider:
            return HttpResponse("You're not welcome.", status=status.HTTP_403_FORBIDDEN)
        else:
            return self.get_response(request)


class LoggingMiddleware(deprecation.MiddlewareMixin):
    """
    抽象请求日志记录中间件
    """

    def process_request(self, request):
        if self.__getattribute__('do_log'):
            do_log = self.__getattribute__('do_log')
            do_log(web.HttpRequestDescriptor(request))

        return self.get_response(request)


# ----------------------------------------------------------------------------------------------------------------------


class StdoutLoggingMixin(object):
    """
    标准控制台请求日志特质
    """

    def do_log(self, request_descriptor):

        if request_descriptor is None:
            return

        if not isinstance(request_descriptor, web.HttpRequestDescriptor):
            raise TypeError('wrong type')

        print('-' * 120)
        print(request_descriptor)
        print('-' * 120)


class StdoutLoggingMiddleware(StdoutLoggingMixin, LoggingMiddleware, ):
    """
    请求日志记录中间件

    此中间件输出日志到标准控制台
    """
    pass
