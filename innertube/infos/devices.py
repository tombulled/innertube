from . import models
from . import types

Web = models.DeviceInfo \
(
    name = 'Web',
    type = types.DeviceType.Web,
)

Android = models.DeviceInfo \
(
    name = 'Android',
    type = types.DeviceType.Android,
)

Ios = models.DeviceInfo \
(
    name = 'IOS',
    type = types.DeviceType.Ios,
)
