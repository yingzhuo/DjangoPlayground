"""
随机数/字符串生成工具
"""
import random
import string
import uuid

ALL_ASCII = string.ascii_letters


def random_string(length=32, chars=ALL_ASCII):
    """
    生成随机字符串
    :param length: 要生成的字串长度
    :param chars: 允许出现的字符列表
    :return: 随机字符串
    """
    return ''.join(random.choice(chars) for _ in range(length))


def uuid36():
    """
    获取36位UUID
    :return: 36位UUID
    """
    return str(uuid.uuid4())


def uuid32():
    """
    获取32位UUID
    :return: 32位UUID
    """
    return uuid36().replace('-', '')
