from . import info
from . import services
from . import devices
from . import infos
from . import clients
from .clients import base as clients_base

SERVICE_INFOS = \
{
    key: value
    for key in dir(services)
    if isinstance(value := getattr(services, key), info.ServiceInfo)
}

DEVICE_INFOS = \
{
    key: value
    for key in dir(devices)
    if isinstance(value := getattr(devices, key), info.DeviceInfo)
}

CLIENT_INFOS = \
{
    key: value
    for key in dir(infos)
    if isinstance(value := getattr(infos, key), info.ClientInfo)
}

CLIENTS = \
{
    key: value
    for key in dir(clients)
    if isinstance(value := getattr(clients, key), type) and \
        issubclass(value, clients_base.Client)
}
