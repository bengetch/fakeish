from importlib import import_module
from fakeish.utils.loading import find_objects, get_methods
from fakeish.factory import Factory


class Fakeish:
    def __init__(self):
        self._factory = Factory()

    def __getattr__(self, attr):
        return getattr(self._factory, attr)
