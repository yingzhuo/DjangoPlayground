from enum import Enum

from django_sugar.lang import choices


class Gender(choices.ChoicesType, Enum):
    """
    性别
    """

    # 女
    FEMALE = 0

    # 男
    MALE = 1
