'''
Library containing class decorators for use when declaring Client classes

>>> from innertube.clients import decorators
>>>
>>> dir(decorators)
...
>>>
>>> decorators.method
<function method at 0x7fc1f9e629d0>
>>>
'''

import functools
from typing import Callable
from ..infos.models import ClientInfo
from . import base

def method(func: Callable) -> Callable:
    '''
    Decorator to implement a method for a given Client

    Parameters:
        func: Method to implement

    Returns:
        A class decorator

    Usage:
        >>> def my_method(dispatch):
                return dispatch('some/endpoint')
        >>>
        >>> @method(my_method)
        ... class MyClient(Client): pass
        >>>
        >>> MyClient.my_method
        <function my_method at 0x7fc1f96d4550>
        >>>
    '''

    def decorator(cls: type) -> type:
        '''
        Decorator to decorate a Client class

        Creates a new method on the class that proxies the provided method
        '''

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            '''
            Wrapper that imitates the provided method, and sends a dispatch function
            instead of the Client class instance as the first argument
            '''

            return func(self.adaptor.dispatch, *args, **kwargs)

        setattr(cls, func.__name__, wrapper)

        return cls

    return decorator

def info(client_info: ClientInfo) -> Callable:
    '''
    Decorator to auto-initialise a Client with it's associated ClientInfo

    Parameters:
        client_info: The ClientInfo to initialise the Client class with

    Returns:
        A class decorator

    Usage:
        >>> @info(some_client_info)
        class MyClient(Client): pass
        >>>
        >>> MyClient.__init__
        <function info.<locals>.decorator.<locals>.wrapper at 0x7fc1f96d45e0>
        >>>
        >>> client = MyClient()
        >>>
        >>> client.info
        ...
        >>>
    '''

    def decorator(cls: type) -> type:
        '''
        Decorator to decorate a provided Client class

        Overwrites the __init__ method of the classs to pass through the ClientInfo
        automatically
        '''

        def wrapper(self) -> object:
            '''
            Wrapper that initialises the Client automatically with the provided
            ClientInfo
            '''

            base.Client.__init__(self, client_info)

        setattr(cls, '__init__', wrapper)

        return cls

    return decorator
