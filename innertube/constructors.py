from . import apps

from typing import \
(
    Optional,
    Union,
)

from babel import \
(
    Locale,
)

from .client import \
(
    Client,
)

from .models import \
(
    AppInfo,
    ServiceInfo,
    DeviceInfo,
)

from .enums import \
(
    ServiceType,
    DeviceType,
)

def client \
        (
            service: Union[ServiceInfo, ServiceType],
            device:  Union[DeviceInfo, DeviceType],
            locale:  Locale = None,
        ) -> Optional[Client]:
    if isinstance(service, ServiceInfo): service = service.type
    if isinstance(device, DeviceInfo):   device  = device.type

    for app_name in dir(apps):
        if isinstance(app_info := getattr(apps, app_name), AppInfo) \
                and app_info.service.type == service \
                and app_info.device.type  == device:
            return Client \
            (
                info   = app_info,
                locale = locale,
            )
