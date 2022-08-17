"""
http请求相关工具等
"""
from django.http import HttpRequest


class HttpRequestDescriptor(object):
    """
    http请求描述器
    """

    def __init__(self, request: HttpRequest):
        """
        构造方法
        :param request: 请求对象
        """
        self.request = request

    def get_base_info(self):
        return {
            'schema': self.request.scheme,
            'is_secure': self.request.is_secure(),
            'method': self.request.method,
            'path': self.request.path,
        }

    def get_headers(self):
        return {k: v for k, v in self.request.headers.items()}

    def has_at_least_one_header(self):
        return len(self.get_headers()) > 0

    def get_query_dict(self):
        # return self.request.GET if self.request.method == 'GET' else self.request.POST
        # TODO: 我还没有学明白为什么
        return self.request.GET

    def has_ast_least_one_query_parameter(self):
        return len(self.get_query_dict()) > 0

    def get_detail(self):
        d = list()

        # 请求具体类型
        d.append("Request Type:")
        d.append("\t%s" % type(self.request))

        # 基本信息
        d.append("Base Information:")
        for name, content in self.get_base_info().items():
            d.append("\t%s => %s" % (name, content))

        # 请求头
        if self.has_at_least_one_header():
            d.append("Headers:")
            for name, value in self.get_headers().items():
                d.append("\t%s => %s" % (name, value))

        # query参数
        if self.has_ast_least_one_query_parameter():
            d.append("Query Dict:")
            for k, v in self.get_query_dict().items():
                d.append("\t%s => %s" % (k, v))

        return d

    def __str__(self):
        return '\n'.join(self.get_detail())

    def __repr__(self):
        return str(self)
