'''
Package containing Info objects

These objects are responsible for storing information about various entities
(e.g. Clients, Services, Devices)

Notes:
    * Variables accessible here (e.g `SERVICES`) store maps of all of their Info objects
    * All child modules (excluding utils) are automatically imported (to allow chaining)

Usage:
    >>> from innertube import infos
    >>>
    >>> dir(infos)
    ...
    >>>
    >>> infos.CLIENTS
    ...
    >>>
'''

from . import clients
from . import devices
from . import models
from . import services
from . import types

SERVICES = \
{
    key: value
    for key in dir(services)
    # Only interested in values of type: ServiceInfo
    if isinstance(value := getattr(services, key), models.ServiceInfo)
}

DEVICES = \
{
    key: value
    for key in dir(devices)
    # Only interested in values of type: DeviceInfo
    if isinstance(value := getattr(devices, key), models.DeviceInfo)
}

CLIENTS = \
{
    key: value
    for key in dir(clients)
    # Only interested in values of type: ClientInfo
    if isinstance(value := getattr(clients, key), models.ClientInfo)
}
