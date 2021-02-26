from . import info
from . import types

Web = info.DeviceInfo \
(
    name = 'Web',
    type = types.DeviceType.Web,
)

Android = info.DeviceInfo \
(
    name = 'Android',
    type = types.DeviceType.Android,
)

Ios = info.DeviceInfo \
(
    name = 'IOS',
    type = types.DeviceType.Ios,
)
