'''
Library containing Info objects of type: DeviceInfo

Usage:
    >>> from innertube.infos import devices
    >>>
    >>> dir(devices)
    ...
    >>>
    >>> devices.Web
    DeviceInfo(...)
    >>>
'''

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

Tv = models.DeviceInfo \
(
    name = 'TV',
    type = types.DeviceType.Tv,
)
