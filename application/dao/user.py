"""
User相关数据库存取
"""
from application.models import User


class UserDao(object):
    """
    User相关数据库存取
    """

    @staticmethod
    def find_by_username(username):
        return User.objects.filter(username=username).first()

    @staticmethod
    def find_by_id(pk):
        try:
            return User.objects.filter(id=pk).first()
        except IndexError:
            return None
