'''
Library containing info-related utility functions

Usage:
    >>> from innertube.infos import utils
    >>>
    >>> dir(utils)
    ...
    >>>
    >>> utils.get_client_info
    <function get_client_info at 0x7fc1fc1141f0>
    >>>
'''

from typing import Union
from . import CLIENTS, SERVICES, DEVICES
from .models import ServiceInfo, DeviceInfo, ClientInfo
from .types import ServiceType, DeviceType

def get_client_info \
        (
            *,
            service: Union[ServiceInfo, ServiceType],
            device:  Union[DeviceInfo,  DeviceType],
        ) -> ClientInfo:
    '''
    Utility function that gets the ClientInfo that uses `service` and `device`

    Parameters:
        service: The service the ClientInfo uses
        device:  The device  the ClientInfo uses

    Returns:
        The ClientInfo that uses `service` and `device` or None

    Usage:
        >>> get_client_info \
        (
            service = ServiceType.YouTube,
            device  = DeviceType.Android,
        )
        ClientInfo(...)
        >>>
    '''

    service_type = service if isinstance(service, ServiceType) else service.type
    device_type  = device  if isinstance(device,  DeviceType)  else device.type

    for client_info in CLIENTS.values():
        if client_info.service.type == service_type \
                and client_info.device.type == device_type:
            return client_info

def get_service_info(service: ServiceType) -> ServiceInfo:
    '''
    Utility function that gets the ServiceInfo with type `service`

    Parameters:
        service: The ServiceType of the the ServiceInfo

    Returns:
        The ServiceInfo with type `service`

    Usage:
        >>> get_service_info(ServiceType.YouTube)
        ServiceInfo(...)
        >>>
    '''

    for service_info in SERVICES.values():
        if service_info.type == service:
            return service_info

def get_device_info(device: DeviceType) -> DeviceInfo:
    '''
    Utility function that gets the DeviceInfo with type `device`

    Parameters:
        device: The DeviceType of the the DeviceInfo

    Returns:
        The DeviceInfo with type `device`

    Usage:
        >>> get_device_info(DeviceType.Android)
        DeviceInfo(...)
        >>>
    '''

    for device_info in DEVICES.values():
        if device_info.type == device:
            return device_info
