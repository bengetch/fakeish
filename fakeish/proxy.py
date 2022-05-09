from importlib import import_module
from fakeish.utils.loading import find_objects, get_methods
from fakeish.factory import Factory
import fakeish.unique as unique


class Fakeish:
    def __init__(self, num_rows: int = 0):
        self._factory = Factory()
        if num_rows > 0:
            self.unique = unique.RandomObject(num_rows)

    def __getattr__(self, attr):
        return getattr(self._factory, attr)
