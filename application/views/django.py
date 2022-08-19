import django
from rest_framework.views import APIView

from common.api import API, APIResponse


class DjangoVersionView(APIView):
    """
    Django版本相关信息

    URL:  /v1/django-version/
    """

    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        api = API().add({
            'django_version': django.get_version(),
            'api_version': request.version,
        })
        return APIResponse(api)
