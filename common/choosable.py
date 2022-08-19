class ChoiceMixin(object):
    """
    枚举特质
    """

    @classmethod
    def choices(cls):
        return [(m.name, m.value) for m in cls]

    @classmethod
    def contains_name(cls, name):
        return name in [m.name for m in cls]

    @classmethod
    def contains_value(cls, value):
        return value in [m.value for m in cls]
