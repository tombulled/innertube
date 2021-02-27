'''
Library containing client-related utility functions

>>> from innertube.clients import utils
>>>
>>> dir(utils)
...
>>>
>>> utils.get_client
<function get_client at 0x7fc1fc1141f0>
>>>
'''

from typing import Union
from ..infos.models import ServiceInfo, DeviceInfo
from ..infos.types import ServiceType, DeviceType
from .base import Client
from . import CLIENTS

def get_client \
        (
            *,
            service: Union[ServiceInfo, ServiceType],
            device:  Union[DeviceInfo,  DeviceType],
        ) -> Union[Client, None]:
    '''
    Utility function to get the client that uses `service` and `device`

    Parameters:
        service: The service the client uses
        device:  The device  the client uses

    Returns:
        The client that uses `service` and `device` or None

    Usage:
        >>> get_client \
        (
            service = ServiceType.YouTube,
            device  = DeviceType.Android,
        )
        <Client(device='Android', service='YouTube')>
        >>>
    '''

    service_type = service if isinstance(service, ServiceType) else service.type
    device_type  = device  if isinstance(device,  DeviceType)  else device.type

    for client_class in CLIENTS.values():
        client = client_class()

        if client.info.service.type == service_type and client.info.device.type == device_type:
            return client
