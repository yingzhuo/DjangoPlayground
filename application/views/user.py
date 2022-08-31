r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
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
