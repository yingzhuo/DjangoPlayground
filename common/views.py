"""
通用视图
"""
from django.shortcuts import render


def access_denied(request, exception):
    """
    处理403
    :param request: 请求
    :param exception: 错误
    :return: 应答
    """
    return render(request, '403.html', status=403)


def resource_not_found(request, exception):
    """
    处理404
    :param request: 请求
    :param exception: 错误
    :return: 应答
    """
    return render(request, '404.html', status=404)


def server_internal_error(request):
    """
    处理500
    :param request: 请求
    :return: 应答
    """
    return render(request, '500.html', status=500)
