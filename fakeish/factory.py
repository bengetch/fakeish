from importlib import import_module
from fakeish.utils.loading import find_objects, get_methods


class Factory:
    def __init__(self, module: str):
        self._objects = find_objects([import_module(module)])
        self._load_methods()

    def _load_methods(self):

        for obj in self._objects:
            methods = get_methods(obj)
            for name, func in methods:
                self.set_method(name, func)
    
    def set_method(self, name, func):
        setattr(self, name, func)

