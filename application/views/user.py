import json

from django.http import HttpResponse
from rest_framework.views import APIView

from application.dao.user import UserDao
from application.models.user import UserSerializer
from common.api import APIResponse


class FindUserByIdView(APIView):
    """
    获取单个用户详情

    URL: /v1/user/<userId>/
    """

    def get(self, request, *args, **kwargs):

        user = UserDao.find_by_id(kwargs.get('pk'))

        if user:
            ser = UserSerializer(instance=user, many=False)
            ret = json.dumps(ser.data, ensure_ascii=False)
            return HttpResponse(ret)
        else:
            return APIResponse()
