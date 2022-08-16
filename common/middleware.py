"""
中间件
"""
from django.utils.deprecation import MiddlewareMixin

from common.request import HttpRequestDescriptor


class StdoutLoggingMiddleware(MiddlewareMixin):
    """
    简易的请求日志记录器
    """

    def __int__(self, get_response):
        super().sync_capable = True
        super().async_capable = False
        super().__init__(get_response)

    def process_request(self, request):
        descriptor = HttpRequestDescriptor(request)
        print('-' * 100)
        print(descriptor)
        print('-' * 100)
        return self.get_response(request)
