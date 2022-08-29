"""
配置URL映射
"""

# namespace
from django.urls import re_path

from application.views.django import DjangoVersionView
from application.views.security import LoginView, TokenInfoView
from application.views.temptest import TempTestView
from application.views.user import FindUserByIdView

app_name = 'application'

# url映射
urlpatterns = [
    # 临时测试
    re_path(r'^(?P<version>v[0-9]+)/temp-test/$', TempTestView.as_view()),

    # 版本查看页面
    re_path(r'^(?P<version>v[0-9]+)/django-version/$', DjangoVersionView.as_view()),

    # 登录
    re_path(r'^(?P<version>v[0-9]+)/security/login/$', LoginView.as_view()),
    re_path(r'^(?P<version>v[0-9]+)/security/token/$', TokenInfoView.as_view()),

    # 用户
    re_path(r'^(?P<version>v[0-9]+)/user/(?P<pk>\d+)/$', FindUserByIdView.as_view()),
]
