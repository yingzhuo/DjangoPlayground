from rest_framework import exceptions
from rest_framework.response import Response
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
            return Response(data=ser.data)
        else:
            raise exceptions.NotFound()
