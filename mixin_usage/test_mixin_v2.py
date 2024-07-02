class LoggedMappingMixin:
    """
    add logging to get/set/delete operation for debugging
    """

    __slot__ = ()

    def __getitem__(self, key):
        print(f"Getting {key}")
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        print(f"Setting {key} = {value}")
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print(f"Deleting {key}")

class SetOnceMappingMixin:
    """
    Only allow a key to be set once.
    """

    __slots__ = ()
    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(f"{key} already set")
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    """
    Restrict keys to strings only
    """
    __slots__ = ()
    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise KeyError(f"keys must be strings")
        return super().__setitem__(key, value)


class LoggedDict(LoggedMappingMixin, dict):
    pass

d = LoggedDict()
d['x'] = 23
print(d['x'])
del d['x']

from collections import defaultdict

class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass

d = SetOnceDefaultDict(list)
d['x'].append(2)
d['x'].append(3)
d['x'] = 23

