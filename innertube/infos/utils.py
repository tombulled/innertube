from . import CLIENTS
from .models import ServiceInfo, DeviceInfo
from .types import ServiceType, DeviceType

def get_client_info(*, service: Union[ServiceInfo, ServiceType], device: Union[DeviceInfo, DeviceType]):
    service_type = service if isinstance(service, ServiceType) else service.type
    device_type  = device  if isinstance(device,  DeviceType)  else device.type

    for client_info in CLIENTS.values():
        if client_info.service.type == service_type \
                and client_info.device.type == device_type:
            return client_info
