from enum import Enum

from common.choosable import ChoiceMixin


class Gender(ChoiceMixin, Enum):
    """
    性别
    """

    # 女
    FEMALE = 0

    # 男
    MALE = 1
