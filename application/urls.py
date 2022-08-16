"""
settings URL Configuration
"""

# namespace
from django.urls import path

from application.views import TestView

app_name = 'application'

# url映射
urlpatterns = [
    path('test/', TestView.as_view()),
]
