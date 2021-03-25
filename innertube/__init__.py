'''
Package to facilitate low-level communication with Google's InnerTube API
'''

from babel import \
(
    Locale,
)

from .infos import \
(
    services,
    devices,
    clients,
    apps,
)

from .sessions import \
(
    Session,
)

from .clients import \
(
    Client,
)

from .enums import \
(
    DeviceType,
    ServiceType,
)

from .errors import \
(
    InnerTubeException,
)

def client \
        (
            service: ServiceType,
            device:  DeviceType,
            locale:  Locale = None,
        ) -> Client:
    return Client \
    (
        info = apps.get \
        (
            service = services.get(type = service),
            device  = devices.get(type  = device),
        ),
        locale = locale,
    )
