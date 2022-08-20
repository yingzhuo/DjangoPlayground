import json

import django
import rest_framework
from django.http import HttpResponse
from rest_framework.views import APIView


class DjangoVersionView(APIView):
    """
    Django版本相关信息

    URL:  /v1/django-version/
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        ret = {
            'django_core_version': django.get_version(),
            'django_rest_version': rest_framework.VERSION
        }

        return HttpResponse(
            json.dumps(ret, ensure_ascii=False),
            content_type='application/json; charset=utf-8'
        )
