from . import infos
from . import clients
from .clients import base as clients_base

SERVICE_INFOS = \
{
    key: value
    for key in dir(infos.services)
    if isinstance(value := getattr(infos.services, key), infos.models.ServiceInfo)
}

DEVICE_INFOS = \
{
    key: value
    for key in dir(infos.devices)
    if isinstance(value := getattr(infos.devices, key), infos.models.DeviceInfo)
}

CLIENT_INFOS = \
{
    key: value
    for key in dir(infos.clients)
    if isinstance(value := getattr(infos.clients, key), infos.models.ClientInfo)
}

CLIENTS = \
{
    key: value
    for key in dir(clients)
    if isinstance(value := getattr(clients, key), type) and \
        issubclass(value, clients_base.Client)
}
