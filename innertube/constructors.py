from . import apps

from typing import \
(
    Optional,
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
    ServiceInfo,
    DeviceInfo,
    AppInfo,
)

def client \
        (
            service: ServiceInfo,
            device:  DeviceInfo,
            locale:  Locale = None,
        ) -> Optional[Client]:
    for app_name in dir(apps):
        if isinstance(app_info := getattr(app_name, key), AppInfo) \
                and app_info.service == service \
                and app_info.device  == device:
            return Client \
            (
                info   = app_info,
                locale = locale,
            )
