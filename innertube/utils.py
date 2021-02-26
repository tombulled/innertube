from . import maps
from .infos.models import ServiceInfo, DeviceInfo, ClientInfo
from .infos.types import ServiceType, DeviceType
from typing import Union, Callable, Iterable

def get_client_info(*, service: Union[ServiceInfo, ServiceType], device: Union[DeviceInfo, DeviceType]):
    service_type = service if isinstance(service, ServiceType) else service.type
    device_type  = device  if isinstance(device,  DeviceType)  else device.type

    for client_info in maps.CLIENT_INFOS.values():
        if client_info.service.type == service_type \
                and client_info.device.type == device_type:
            return client_info

def get_client(*, service: Union[ServiceInfo, ServiceType], device: Union[DeviceInfo, DeviceType]):
    service_type = service if isinstance(service, ServiceType) else service.type
    device_type  = device  if isinstance(device,  DeviceType)  else device.type

    for client_class in maps.CLIENTS.values():
        client = client_class()

        if client.info.service.type == service_type and client.info.device.type == device_type:
            return client

def build_user_agent(client_info: ClientInfo):
    builders = \
    {
        DeviceType.Web: lambda: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        DeviceType.Android: lambda: '{package}/{client_version}(Linux; U; Android 9; en_GB; VirtualBox Build/PI)'.format \
        (
            package = client_info.service.packages.get(client_info.device.type),
            client_version = client_info.version,
        ),
        DeviceType.Ios: lambda: '{package}/{client_version} (iPhone10,5; U; CPU iOS 14_4 like Mac OS X; en_GB)'.format \
        (
            package = client_info.service.packages.get(client_info.device.type),
            client_version = client_info.version,
        ),
    }

    device_type = client_info.device.type

    if device_type not in builders:
        device_type = DeviceType.Web

    return builders.get(device_type)()

def url(*, domain: str, scheme: str = 'https', port: Union[int, None] = None, endpoint: Union[str, None] = None):
    return '{scheme}://{domain}{sep_port}{port}/{endpoint}'.format \
    (
        scheme   = scheme,
        domain   = domain,
        sep_port = ':' if port else '',
        port     = port or '',
        endpoint = endpoint.lstrip(r'\/') if endpoint else '',
    )

def filter \
        (
            iterable: Iterable,
            func:     Callable = None,
        ) -> Iterable:
    '''
    Filter an iterable.

    Return an iterable containing those items of iterable for which func(item),
    or func(key, value) if the iterable is a dict, are true.

    Args:
        iterable: An iterable to filter
        func: A function to filter items by
            Note: If the iterable *is* a dictionary, the function signature
                is func(key: Any, value: Any) -> bool
            Note: If the iterable is *not* a dictionary, the function signature
                is func(item: Any) -> bool
    Returns:
        If isinstance(iterable, dict):
            Returns dict
        Else:
            Returns list
    Example:
        If isinstance(iterable, dict):
            >>> data = {'a': 1, 'b': None, 'c': 3}
            >>> filter(data)
            {'a': 1, 'c': 3}
            >>>
        Else:
            >>> data = [1, None, 3]
            >>> filter(data)
            [1, 3]
            >>>
    '''

    if isinstance(iterable, dict):
        if not func:
            func = lambda key, val: val is not None

        return \
        {
            key: val
            for key, val in iterable.items()
            if func(key, val)
        }
    else:
        if func is None:
            func = lambda item: item is not None

        return \
        [
            val
            for val in iterable
            if func(val)
        ]
