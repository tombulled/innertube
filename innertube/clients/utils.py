from typing import Union
from ..infos.models import ServiceInfo, DeviceInfo
from ..infos.types import ServiceType, DeviceType
from . import CLIENTS

def get_client(*, service: Union[ServiceInfo, ServiceType], device: Union[DeviceInfo, DeviceType]):
    service_type = service if isinstance(service, ServiceType) else service.type
    device_type  = device  if isinstance(device,  DeviceType)  else device.type

    for client_class in CLIENTS.values():
        client = client_class()

        if client.info.service.type == service_type and client.info.device.type == device_type:
            return client
