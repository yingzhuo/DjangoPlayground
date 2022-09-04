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
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAx5/n6FD3mUBbd7m2o/Xu
qs8dmFqIQFfScz0c8TfkyS7CQJJ7swiGv+OzExXmhP5tbFmF7Pt4Mw930onGVvWi
qz9VtG13HYaUoTy4Sa78vbvDBZl/FpDYXPfGVVUJz2w9ThWNjnHD4wlPZwC2BzBK
gPm0u0XodisMQ3iDVEah+jECmf/quO1BwhYyBdU7xGB6/R3OsfvtFY5QZfAxBbHW
/gBnWm3Ta6ARw/MPpm6VzocO3QN5qg2O+HSm9KwoXo2tDsWYmxJucySCebJdKVF7
A8BUTjHArDV4osP0sF2KMLm75adri/qzqFt/KOuOI8Zg/oAhnYBqqT4vitJWhbYQ
1QIDAQAB
-----END PUBLIC KEY-----
"""

_RSA_PRIVATE_KEY = b"""
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-256-CBC,B10EE00ABB5235B022EB44F5056568DB

6FgAOLzYxFuDF02IKa+KNSDMw4NbPSaOrO2YO8QhRmkcNPcqr4+Drz8yBoRtm038
TKOGwqQb9IRTqymOG58U6e7uc9THUYeHzxPg0pPwClpbhNOB6wnF2K+VapaIigdQ
jgXD3Bpztg7Ux72z6Sy/04L++IFOST72I5QEll89JkSaHrMfPtgLgCVs7GftjmzI
OYQaD3R5DS55iQjlbMGtQ+yjC/fdRg/++rAvJx17Pww352ltsBlCD2G0TgTW1YZO
3vuTHeAJUKNm6jM9fa9C/kk/eAe/2j3y5Ni+H4jruXKvjJ4TmTwdWejHKJguqYt+
fm504LmxQqC04y63ecUvY1shb7qEdNqxa83YI2xUeYHL9KN6WO6KWTma9quAq6s0
fA0r8GZP78gmlrthgqgwYnQgukds9NKrQZ17pjUfUXku99e/S4E2nbLEkCBm4Xa6
MKxTBqq5NdKnWvWxiTZWQ06c4HEYx3Lbt0afy0sGYOqMvW2Em2irB1miXFMEn7j7
fSw0i5ubUOes3rQfmCczsgMVT5mJQjO3kebNxZMdbMfHDpXiI8yAwAAu4WEjdntT
RbXSQsJ6dw6lINyalqruMZscNsNH7gdEe725oymATa9WNeluym9c3NhtpSdSOE41
LiQMMkywQMsavucU6RdLPA1tQmsj1DiV/crfz0FhoKr9b8a43EitElo42X1fskYR
YAskbJneaEAiG9aAGMxU5YVwDyS7aECQLN83GOVOCxmTtlx4gPdUX+ZlDwSHoyeH
adYHTXJSXLc7wXYJyFtnmXgXf2VZROgF/9f4k3hROQj4/A//2nXa4+QZNzYrMGyh
ZhLR25CFUzVgCcxo64IEm4aRL5PEzqX3Xk6Bu6OwROCWdiqRHD6R5FnL1AbPLJgE
tPgJRKWrzjsCOB98wJhuRgbuCU//yBQ2aQmaWxwcDeCurIBGFrei945SpKNj0ulA
QmpkbLQCt3lbwVpVQd+5F3D11EbXfiOXVOSKQlVxp6szIsB0RKem5lcLza3satwN
EblYrVI/cWpmutaVGoNXj/0qW6bBqrbX86NtTEVy75WQhB1xrUNhGwZJL+J/mPYN
5YdYANIBHPURNSAUHSQF/oZq58SHoD19ZjWoX44pkHtYkwNifilUN0kwwKIKd56e
GORK90gUytcjgNcAjwcebga7GgYlIQeN4KxJr5libeUczBSpxcO68JuopgH260nO
3kUwAHTubzEK6dlHpgQ7gd280h87jaJR3ccpNL0b0xekhdQMsgw/ZE+kFkhb3+Zm
LKz6J475fHmXDMCP06DembIEYj+3KRnTNN/gJ6Vl7Poc47ux/5LJ2JCID3+3CMUV
/NelQJvLnhjDozHgFpt1plSFc91b7Jvn5FxGtTonMvtctSVfeIS+pTm1xdOqtNak
gpZvDsNlthrEFcvJJ0+C8UGYj354qlZEw1nBL9z6+xNstsj6ptL/G1Lmc7SSZmFn
zuK5q4KiljpkfLtjGYXeoBCCqNn4f/z/aPbxXwslrK95Rw4jEiTA6lUkdLOPmvl0
ntCsXqdl6ec9oQv8i3D3sDtAL3rpY3f7dyduNhaYMRqdltkleZZ3aa2XuJsXnRHz
-----END RSA PRIVATE KEY-----
"""

JWT_SECRET_KEY = web.create_rs384_algorithm(
    public_key=_RSA_PUBLIC_KEY,
    private_key=_RSA_PRIVATE_KEY,
    passphrase=b'DjangoPlayground',
)


# ----------------------------------------------------------------------------------------------------------------------

def get_current_user_id(request):
    if request:
        try:
            return request.user['id']
        except (AttributeError, TypeError, ValueError,):
            return -1
    return -1


def get_current_user_username(request):
    if request:
        try:
            return request.user['username']
        except (AttributeError, TypeError, ValueError,):
            return '(Unknown)'
    return '(Unknown)'


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
