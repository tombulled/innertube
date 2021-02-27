'''
Package containing InnerTube Clients

The variable `CLIENTS` stores a map of all of client classes

>>> from innertube.clients import clients
>>>
>>> dir(clients)
...
>>>
>>> clients.CLIENTS
...
>>>
'''

from . import base
from .clients import *

CLIENTS = \
{
    key: value
    for key in dir(clients)
    # Only interested if the value is a class, and that class inherits from the base Client
    if isinstance(value := getattr(clients, key), type) and \
        issubclass(value, base.Client)
}
