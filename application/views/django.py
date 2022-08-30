r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
import django
import django_sugar
import rest_framework
from rest_framework.response import Response
from rest_framework.views import APIView


class DjangoVersionView(APIView):
    """
    Django版本相关信息

    URL:  /v1/django-version/
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        data = {
            'django_core_version': django.get_version(),
            'django_rest_version': rest_framework.VERSION,
            'django_sugar_version': django_sugar.VERSION,
        }
        return Response(data)
