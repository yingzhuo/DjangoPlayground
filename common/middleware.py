r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
import logging

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
    请求日志记录中间件
    """

    def process_request(self, request):
        descriptor = web.HttpRequestDescriptor(request)
        logging.debug('-' * 120)
        for msg in descriptor.get_detail():
            logging.debug(msg)
        logging.debug('-' * 120)
        return self.get_response(request)
