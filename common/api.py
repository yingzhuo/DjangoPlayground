from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse

# 返回码 - OK
CODE_OK = '10000'


class API(object):
    code = CODE_OK
    error = None
    payload = dict()

    def __int__(self, *, code=None, error=None, **kwargs):
        code = code or CODE_OK
        self.code = code
        self.error = error
        self.payload = {k: v for k, v in kwargs.items()}

    def clean(self):
        for k, _ in self.payload.items():
            del self.payload[k]

    def add(self, data_dict):
        if not isinstance(data_dict, dict):
            raise TypeError('data_dict is not a dict')

        for k, v in data_dict.items():
            self.payload[k] = v

        return self

    def as_dict(self):
        ret = dict()
        ret['code'] = self.code
        ret['error'] = self.error
        ret['payload'] = self.payload
        return ret

    def __getitem__(self, item):
        return self.payload[item]


class APIResponse(JsonResponse):

    def __init__(
            self,
            dict_or_api,
            encoder=DjangoJSONEncoder,
            safe=True,
            json_dumps_params=None,
            **kwargs,
    ):
        if isinstance(dict_or_api, API):
            dict_or_api = dict_or_api.as_dict()

        json_dumps_params = {"ensure_ascii": False, **(json_dumps_params or {})}
        super().__init__(dict_or_api, encoder, safe, json_dumps_params=json_dumps_params, **kwargs)
