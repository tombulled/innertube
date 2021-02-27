from . import base
from .clients import *

CLIENTS = \
{
    key: value
    for key in dir(clients)
    if isinstance(value := getattr(clients, key), type) and \
        issubclass(value, base.Client)
}
