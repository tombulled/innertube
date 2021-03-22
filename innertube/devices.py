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

Web = models.DeviceInfo \
(
    name          = 'Web',
    product_token = '(Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
)

Android = models.DeviceInfo \
(
    name          = 'Android',
    product_token = '(Linux; U; Android 9; en_GB; VirtualBox Build/PI)',
    package       = 'com.google.android',
)

Ios = models.DeviceInfo \
(
    name          = 'IOS',
    product_token = '(iPhone10,5; U; CPU iOS 14_4 like Mac OS X; en_GB)',
    package       = 'com.google.ios',
)

Tv = models.DeviceInfo \
(
    name          = 'TV',
    product_token = '(PlayStation; PlayStation 4/8.03) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15',
)
