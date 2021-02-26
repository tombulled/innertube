from . import info
from . import services
from . import devices
from . import infos

SERVICES = \
{
    key: value
    for key in dir(services)
    if isinstance(value := getattr(services, key), info.ServiceInfo)
}

DEVICES = \
{
    key: value
    for key in dir(devices)
    if isinstance(value := getattr(devices, key), info.DeviceInfo)
}

CLIENTS = \
{
    key: value
    for key in dir(infos)
    if isinstance(value := getattr(infos, key), info.ClientInfo)
}
