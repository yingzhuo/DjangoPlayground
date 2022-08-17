"""
配置URL映射
"""

# namespace
from django.urls import path

from application.views.django import DjangoVersionView
from application.views.security import LoginView, TokenInfoView

app_name = 'application'

# url映射
urlpatterns = [
    path('django-version/', DjangoVersionView.as_view()),
    path('security/login/', LoginView.as_view()),
    path('security/token/', TokenInfoView.as_view()),
]
