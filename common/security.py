r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""

from django_sugar import web
from rest_framework import permissions, throttling

_RSA_PUBLIC_KEY = b"""
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwCyA7heAPFj6a0+zOFyy
tszq+4dAloRi2DAbhakW5pA0oRJ4V/uKFFyKgUOjlt93Et/T0+7GyO7nRum0QhRI
AClF20sX937e7Ppu5WaImqGVR4AHVQbS3fY2aVy5bqH/gmFj+h6T8PMPwZo2Rluf
LdSB3N/cUN9tYZG4iAvIY8hWVqJoNSNpbDZXO4M3dcKGecdSbBvpIhjtOK5mVitA
dvxmWWRyGgiG8jOdsetwVh5IscUk4iEm3SX0qDr/ZDqmvhowB2w2yyMAZchQOxEG
T6EwJvzjxt5r5ZhMDwuXTQqL6LNj7k6mqBgqvpk23ubjDhK6c3HlV+02OItjhoLw
QQIDAQAB
-----END PUBLIC KEY-----
"""

_RSA_PRIVATE_KEY = b"""
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAwCyA7heAPFj6a0+zOFyytszq+4dAloRi2DAbhakW5pA0oRJ4
V/uKFFyKgUOjlt93Et/T0+7GyO7nRum0QhRIAClF20sX937e7Ppu5WaImqGVR4AH
VQbS3fY2aVy5bqH/gmFj+h6T8PMPwZo2RlufLdSB3N/cUN9tYZG4iAvIY8hWVqJo
NSNpbDZXO4M3dcKGecdSbBvpIhjtOK5mVitAdvxmWWRyGgiG8jOdsetwVh5IscUk
4iEm3SX0qDr/ZDqmvhowB2w2yyMAZchQOxEGT6EwJvzjxt5r5ZhMDwuXTQqL6LNj
7k6mqBgqvpk23ubjDhK6c3HlV+02OItjhoLwQQIDAQABAoIBAEAvXQyousLtMQ6g
ewqLI4GcpatG/FKJev4b60VUOXrelUVrBtjUAcVVN0l/Tuc4Uevy6Cwz5x77dDGi
IvujDH1JS7S3uxSFwm1CI8Ho4h1LdLGB2HEUq19JOdktCB4ka1OftaW3itACTrPq
DtCnD15eSNV9y3cTeNQKuKhvzwlMLfO1PLTBwcu2KhhBQAoT5+mBIhzIe2YGkWik
cHkXvPlkJ6jqHawIXH3jX9G6ynbDcljjgRy/ZgZ8nuIFKWPzp0tkq6xU+dtCiu8I
TYCUyHL7Mhto2NCqglo5odref+/PfnkpoadpP1eomR52sil9v9UmLfvIYFrpOeqz
qxnJn1UCgYEA+/JBdOtXnUusPSZ3037SezMs8te4nEwuX8PyqYaDAgFEMPSsegA1
yxfjtGyDH9VT2jOYg8FkLkLpCiAvSGOnzu4SX1T9485k9Tykd7E0WrJ/HAyWr9hM
/0gUsq9CzRvVvgEjTSRaB/LC+Z0R+c3zF4hxobgD0iHZ8tIfrQqIohsCgYEAw0QM
7QsCiXU/36WwVqzBK0r8/kNv8NJ6aYl7k0xN04cM8+AJiZnsFU7JtdJsUt7qiLu9
kfS+80VPb/Hab/ySwh3+BoHjN5sL1sU5Q/k70tTFrB/KlORppen9gr/bkCr3tFGv
eEfwcpUx0OaV9KhxijRbpd9RoVp55GZAC2wlPNMCgYEA9brifNbNLW2RIFNUq8MW
J3NSc8hTFp523JCRLSc0v8/cYqNBVfy+esdiH6d2fKXkkv2f02HcBALeqDGb7E7G
bN1mrfSHbJjxfv8Wqmb7WTqfHwxoLDobXyE+jsjBrqtnXVpew+6goP/1it/XmH12
i41YxxJjJ6A8osiufGe5u+ECgYEAhMDjONVfaCy6vEZdWNAilFhrIEKg/E1cxBug
VEhwMPuEJtmOImrvQp1KLb9dvgmn0kYxX+XRXHsmwqjfJXvGGwthBPORkuBqcB2u
DTSJI5FcwuTqScfwu8gVfqsJjz5nIcTXUyM1qfEc6TWbhbZvWtK17FOjn9tvO4T4
zcs8ldkCgYEAmp0cKDcO1d8iHq4GNc2d769vpbtVcgS8x29aDeXX/Aly4CcoXeX0
PtEZmZf9E43F36GQ1djzJfEqPEqH63Sdo60Uk0JFV4g83j72RVywhGAwIvbk9BEh
HJh1S8Az/RYpV1nZT9mPid7utLORYaGXmABlRL6qZa6z4nIy2MPya+w=
-----END RSA PRIVATE KEY-----
"""

JWT_SECRET_KEY = web.create_rs384_algorithm(
    public_key=_RSA_PUBLIC_KEY,
    private_key=_RSA_PRIVATE_KEY,
)


# ----------------------------------------------------------------------------------------------------------------------


class TokenBasedAuthenticator(web.TokenBasedAuthenticator,
                              web.CompositeTokenResolver,
                              web.JwtTokenBasedUserFinder):
    # JWT加密key
    jwt_algorithm_and_key = JWT_SECRET_KEY

    @staticmethod
    def convert_user(user_dict):
        # 可以从用户字典转换到其他实体
        return user_dict


# ----------------------------------------------------------------------------------------------------------------------


class RoleUser(permissions.BasePermission):
    """
    用户角色

    只要认证了，都赋予此角色
    """

    def has_permission(self, request, view):
        # 只要认证了，都赋予此角色
        return request.user is not None


# ----------------------------------------------------------------------------------------------------------------------

class NullThrottle(throttling.BaseThrottle):
    """
    请求限流器

    本项目不启用限流功能
    """

    def allow_request(self, request, view):
        return True

    def get_ident(self, request):
        """
        用户ID作为缓存的key
        :param request: 请求对象
        :return: 用户ID
        """
        return str(request.user.id)
