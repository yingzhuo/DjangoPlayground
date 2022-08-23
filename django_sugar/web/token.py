# ----------------------------------------------------------------------------------------------------------------------
#  ____                           ____
# |  _ \(_) __ _ _ __   __ _  ___/ ___| _   _  __ _  __ _ _ __
# | | | | |/ _` | '_ \ / _` |/ _ \___ \| | | |/ _` |/ _` | '__|
# | |_| | | (_| | | | | (_| | (_) |__) | |_| | (_| | (_| | |
# |____// |\__,_|_| |_|\__, |\___/____/ \__,_|\__, |\__,_|_|
#    |__/             |___/                  |___/
#
# https://github.com/yingzhuo/django-sugar
# ----------------------------------------------------------------------------------------------------------------------
import abc

from django_sugar.lang import strtool, base64, uuid, codec


class TokenResolver(object, metaclass=abc.ABCMeta):
    """
    令牌解析器

    本组件只有一个功能，即从一次Http请求中获取令牌。
    本类是抽象的。
    """

    @abc.abstractmethod
    def resolve_token(self, request, **kwargs):
        """
        从Http请求实例中获取令牌
        :param request: 请求实例
        :param kwargs: 其他可选参数
        :return: 令牌，一般是字符串类型
        """


class CompositeTokenResolver(TokenResolver):
    """
    复合型令牌解析器

    代理其他类型令牌解析器，并将第一个能正确解析出令牌的解析的结果返回。
    """

    token_resolver_classes = None

    def __init__(self, **kwargs):
        if self.token_resolver_classes is None:
            self.token_resolver_classes = kwargs.get('token_resolver_classes', [])

    def __len__(self):
        return len(self.token_resolver_classes)

    def resolve_token(self, request, **kwargs):
        for token_resolver in self.get_token_resolvers():
            # noinspection PyBroadException
            try:
                ret = token_resolver.resolve_token(request, kwargs)
                if ret is not None:
                    return ret
            except Exception:
                continue
        return None

    def get_token_resolvers(self):
        return [x() for x in self.token_resolver_classes]


class QueryTokenResolver(TokenResolver):
    """
    令牌解析器具体实现

    从请求参数中获取令牌数据
    """

    token_parameter_name = None

    def __init__(self, **kwargs):
        if self.token_parameter_name is None:
            self.token_parameter_name = kwargs.get('token_parameter_name', '_token')

    def resolve_token(self, request, **kwargs):
        token_value = request.GET.get(self.token_parameter_name, None)
        token_value = strtool.blank_to_none(token_value)
        return token_value


class HeaderTokenResolver(TokenResolver):
    """
    令牌解析器具体实现

    从请求头中获取令牌数据
    """

    # 请求头名
    header_name = None

    # 期望的令牌的前缀
    token_value_prefix = None

    def __init__(self, **kwargs):
        if self.header_name is None:
            self.header_name = kwargs.get('header_name', 'Authorization')

        if self.token_value_prefix is None:
            self.token_value_prefix = kwargs.get('token_value_prefix', 'Token ')

    def resolve_token(self, request, **kwargs):
        token_value = request.headers.get(self.header_name, None)
        token_value = strtool.blank_to_none(token_value)

        if token_value is None or not token_value.startswith(self.token_value_prefix):
            # 找不到此请求头或者值不以指定的前缀开始
            return None
        else:
            return token_value[len(self.token_value_prefix):]


class BearerTokenResolver(HeaderTokenResolver):
    """
    令牌解析器具体实现

    用于解析BearerToken
    """

    header_name = 'Authorization'
    token_value_prefix = 'Bearer '


class BasicTokenResolver(HeaderTokenResolver):
    """
    令牌解析器具体实现

    用于解析BasicToken
    """

    header_name = 'Authorization'
    token_value_prefix = 'Basic '

    def resolve_username_and_password(self, request, **kwargs):
        token = self.resolve_token(request, **kwargs)
        if token:
            uap = base64.base64_standard_decode(token).split(':', 2)
            return uap[0], uap[1]
        else:
            return None, None


class FixedTokenResolver(TokenResolver):
    """
    令牌解析器具体实现

    总是解析出固定的令牌
    """
    fixed_token = None

    def __init__(self, **kwargs):
        if self.fixed_token is None:
            self.fixed_token = kwargs.get('fixed_token', None)

    def resolve_token(self, request, **kwargs):
        return self.fixed_token


class AlwaysNoneTokenResolver(TokenResolver):
    """
    令牌解析器具体实现

    永远不能解析出令牌
    """

    def resolve_token(self, request, **kwargs):
        return None


# ----------------------------------------------------------------------------------------------------------------------

class TokenGenerator(object, metaclass=abc.ABCMeta):
    """
    令牌生成器

    本类是抽象的。
    """

    def generate_token(self, user, **kwargs):
        """
        为用户生成令牌
        :param user: 用户对象
        :param kwargs: 其他参数
        :return: 令牌字符串
        """


class RandomUUIDTokenGenerator(TokenGenerator):
    """
    令牌生成器具体实现

    生成随机UUID作为令牌
    """

    remove_uuid_hyphen = False

    def generate_token(self, user, **kwargs):
        return uuid.random_uuid(remove_hyphen=self.remove_uuid_hyphen)


class MD5TokenGenerator(TokenGenerator):
    """
    令牌生成器具体实现

    使用MD5信息摘要发生成令牌
    """

    def generate_token(self, user, **kwargs):
        return codec.md5(str(user))


# ----------------------------------------------------------------------------------------------------------------------


class TokenBasedUserFinder(object, metaclass=abc.ABCMeta):
    """
    通过token获取用户实例的组件
    """

    @abc.abstractmethod
    def get_user_by_token(self, token, **kwargs):
        """
        从令牌中获取用户信息
        :param token: 令牌
        :param kwargs: 其他参数
        :return: 用户信息
        """
