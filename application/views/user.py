import json

from django.http import HttpResponse
from rest_framework import exceptions
from rest_framework.views import APIView

from application.dao.user import UserDao
from application.models.user import UserSerializer


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
            return HttpResponse(ret, content_type='application/json; charset=utf-8')
        else:
            raise exceptions.NotFound()
