from . import clients
from . import devices
from . import models
from . import services
from . import types

SERVICES = \
{
    key: value
    for key in dir(services)
    if isinstance(value := getattr(services, key), models.ServiceInfo)
}

DEVICES = \
{
    key: value
    for key in dir(devices)
    if isinstance(value := getattr(devices, key), models.DeviceInfo)
}

CLIENTS = \
{
    key: value
    for key in dir(clients)
    if isinstance(value := getattr(clients, key), models.ClientInfo)
}
