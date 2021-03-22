'''
Library containing info object instances of type: DeviceInfo

Usage:
    >>> from innertube import devices
    >>>
    >>> dir(devices)
    ...
    >>>
    >>> devices.Web
    DeviceInfo(...)
    >>>
'''

from . import models
from . import enums

Web = models.DeviceInfo \
(
    type    = enums.DeviceType.WEB,
    name    = 'Web',
    product = models.ProductInfo \
    (
        name    = 'Mozilla',
        version = '5.0',
        token   = 'Windows NT 10.0; Win64; x64; rv:77.0',
    ),
)

Android = models.DeviceInfo \
(
    type    = enums.DeviceType.ANDROID,
    name    = 'Android',
    package = 'com.google.android',
    product = models.ProductInfo \
    (
        token = 'Linux; U; Android 9; en_GB; VirtualBox Build/PI',
    ),
)

Ios = models.DeviceInfo \
(
    type    = enums.DeviceType.IOS,
    name    = 'IOS',
    package = 'com.google.ios',
    product = models.ProductInfo \
    (
        token = 'iPhone10,5; U; CPU iOS 14_4 like Mac OS X; en_GB',
    ),
)

Tv = models.DeviceInfo \
(
    type    = enums.DeviceType.TV,
    name    = 'TV',
    product = models.ProductInfo \
    (
        name    = 'Mozilla',
        version = '5.0',
        token   = 'PlayStation; PlayStation 4/8.03',
    ),
)
