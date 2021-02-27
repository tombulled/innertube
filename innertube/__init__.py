from . import clients
from .infos import devices
from .infos import services

from .utils import get_client as client

CLIENTS = \
{
    key: value
    for key in dir(clients)
    if isinstance(value := getattr(clients, key), type) and \
        issubclass(value, clients.base.Client)
}
