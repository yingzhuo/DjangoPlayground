"""
User相关数据库存取
"""
from application.models import User, UserToken


class UserDao(object):
    """
    User相关数据库存取
    """

    @staticmethod
    def find_by_username_and_password(username, password):
        try:
            return User.objects.filter(username=username, password=password).first()
        except IndexError:
            return None

    @staticmethod
    def find_by_current_token(current_token):
        try:
            user_token = UserToken.objects.filter(token_value=current_token).first()
            return User.objects.filter(user_token=user_token).first()
        except IndexError:
            return None

    @staticmethod
    def find_by_id(pk):
        try:
            user = User.objects.filter(id=pk).first()
            return user
        except IndexError:
            return None
