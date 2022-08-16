"""
配置URL映射
"""

# namespace
from django.urls import path

from application.views.django import DjangoVersionView

app_name = 'application'

# url映射
urlpatterns = [
    path('django-version/', DjangoVersionView.as_view()),
]
