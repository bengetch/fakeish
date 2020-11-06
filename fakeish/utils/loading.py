import os
from pkgutil import iter_modules
from importlib import import_module


def list_module(module):
    path = os.path.dirname(os.path.realpath(module.__file__))
    return [name for _, name, is_pkg in iter_modules([path]) if is_pkg]


def find_objects(modules):

    ret = set()
    for mod in modules:
        objects = [".".join([mod.__package__, m]) for m in list_module(mod) if mod != "__pycache__"]
        ret.update(objects)
    return sorted(ret)


def get_methods(module):

    ret = []
    m = import_module(module)
    obj = m.RandomObject

    for method_name in dir(obj):
        if method_name.startswith("_"):
            continue
        ret.append((method_name, getattr(obj, method_name)))

    return ret
