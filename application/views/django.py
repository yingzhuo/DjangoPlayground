import django
import rest_framework
from rest_framework.views import APIView

from common.api import API, APIResponse


class DjangoVersionView(APIView):
    """
    Django版本相关信息

    URL:  /django-version/
    """

    def get(self, request, *args, **kwargs):
        api = API().add({
            'django_version': django.get_version(),
            'django_restful_framework_version': rest_framework.__version__
        })
        return APIResponse(api)
