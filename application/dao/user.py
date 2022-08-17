"""
User相关数据库存取
"""
from application.models import User


class UserDao(object):
    """
    User相关数据库存取
    """

    @staticmethod
    def find_by_username_and_password(username, password):
        user_list = User.objects.filter(username=username, password=password)
        return user_list[0] if len(user_list) > 0 else None

    @staticmethod
    def find_by_current_token(current_token):
        user_list = User.objects.filter(current_token=current_token)
        return user_list[0] if len(user_list) > 0 else None
