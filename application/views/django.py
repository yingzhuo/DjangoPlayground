import django
import rest_framework
from rest_framework.views import APIView

from common.api import API, APIResponse


class DjangoVersionView(APIView):
    """
    Django版本相关信息
    """

    def get(self, request, *args, **kwargs):
        api = API.new_instance()
        api.add({
            'django_version': django.get_version(),
            'django_restful_framework_version': rest_framework.__version__
        })
        return APIResponse(api)
