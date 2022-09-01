r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""

# namespace
from django.urls import re_path

from application.views.django import DjangoVersionView
from application.views.fileupload import FileUploadView
from application.views.security import LoginView, TokenInfoView
from application.views.user import FindUserByIdView

app_name = 'application'

# url映射
urlpatterns = [
    # 版本查看页面
    re_path(r'^(?P<version>v[0-9]+)/django-version/$', DjangoVersionView.as_view()),

    # 通用文件上传接口
    re_path(r'^(?P<version>v[0-9]+)/file-upload/$', FileUploadView.as_view()),

    # 登录
    re_path(r'^(?P<version>v[0-9]+)/security/login/$', LoginView.as_view()),
    re_path(r'^(?P<version>v[0-9]+)/security/token/$', TokenInfoView.as_view()),

    # 用户
    re_path(r'^(?P<version>v[0-9]+)/user/(?P<pk>\d+)/$', FindUserByIdView.as_view()),
]
