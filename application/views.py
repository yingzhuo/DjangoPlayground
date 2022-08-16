from rest_framework.views import APIView

from common.api import APIResponse, API


class TestView(APIView):

    def get(self, request, *args, **kwargs):
        api = API.new_instance(name='应卓', age=40)
        return APIResponse(api)
