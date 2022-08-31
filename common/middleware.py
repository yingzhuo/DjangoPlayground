r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
import re

from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django_sugar.web import http
from rest_framework import status


class SpiderDenyingMiddleware(MiddlewareMixin):
    """
    拒绝蜘蛛用的Middleware
    """

    def process_request(self, request):
        user_agent = request.headers.get('User-Agent', None)
        if not user_agent:
            return self.get_response(request)

        regex = r"qihoobot|Baiduspider|Googlebot|Googlebot-Mobile|Googlebot-Image|Mediapartners-Google|" \
                r"Adsbot-Google|Feedfetcher-Google|Yahoo! Slurp|Yahoo! Slurp China|YoudaoBot|Sosospider|" \
                r"Sogou spider|Sogou web spider|MSNBot|ia_archiver|Tomato Bot"

        maybe_spider = bool(re.search(regex, user_agent))
        if maybe_spider:
            return HttpResponse("You're not welcome.", status=status.HTTP_403_FORBIDDEN)
        else:
            return self.get_response(request)


class LoggingMiddleware(MiddlewareMixin):
    """
    抽象请求日志记录中间件
    """

    def process_request(self, request):
        if self.__getattribute__('do_log'):
            do_log = self.__getattribute__('do_log')
            do_log(http.HttpRequestDescriptor(request))

        return self.get_response(request)


# ----------------------------------------------------------------------------------------------------------------------


class StdoutLoggingMixin(object):
    """
    标准控制台请求日志特质
    """

    def do_log(self, request_descriptor):

        if request_descriptor is None:
            return

        if not isinstance(request_descriptor, http.HttpRequestDescriptor):
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
