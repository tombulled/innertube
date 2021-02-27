import functools
from typing import Callable
from . import base

def method(func: Callable):
    def decorator(cls: type):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            return func(self.adaptor.dispatch, *args, **kwargs)

        setattr(cls, func.__name__, wrapper)

        return cls

    return decorator

def info(client_info):
    def decorator(cls: type):
        def wrapper(self):
            base.Client.__init__(self, client_info)

        setattr(cls, '__init__', wrapper)

        return cls

    return decorator
