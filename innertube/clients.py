'''
Library containing info object instances of type: ClientInfo

Notes:
    * Client information last updated: 27/02/2021

Usage:
    >>> from innertube import clients
    >>>
    >>> dir(clients)
    ...
    >>>
    >>> clients.Web
    ClientInfo(...)
    >>>
'''

from . import models
from . import enums

Web = models.ClientInfo \
(
    type       = enums.ClientType.WEB,
    name       = 'WEB',
    version    = '2.20210223.09.00',
    identifier = 'youtube',
)

WebMusic = models.ClientInfo \
(
    type    = enums.ClientType.WEB_MUSIC,
    name    = 'WEB_REMIX',
    version = '0.1',
)

WebKids = models.ClientInfo \
(
    type       = enums.ClientType.WEB_KIDS,
    name       = 'WEB_KIDS',
    version    = '2.1.3',
    identifier = 'youtube-pegasus-web',
)

WebStudio = models.ClientInfo \
(
    type    = enums.ClientType.WEB_STUDIO,
    name    = 'WEB_CREATOR',
    version = '1.20210223.01.00',
)

Android = models.ClientInfo \
(
    type    = enums.ClientType.ANDROID,
    name    = 'ANDROID',
    version = '16.07.34',
)

AndroidMusic = models.ClientInfo \
(
    type       = enums.ClientType.ANDROID_MUSIC,
    name       = 'ANDROID_MUSIC',
    version    = '4.16.51',
    identifier = 'youtube-music-android',
)

AndroidKids = models.ClientInfo \
(
    type    = enums.ClientType.ANDROID_KIDS,
    name    = 'ANDROID_KIDS',
    version = '6.02.3',
)

AndroidStudio = models.ClientInfo \
(
    type    = enums.ClientType.ANDROID_STUDIO,
    name    = 'ANDROID_CREATOR',
    version = '21.06.103',
)

Ios = models.ClientInfo \
(
    type    = enums.ClientType.IOS,
    name    = 'IOS',
    version = '16.05.7',
)

IosMusic = models.ClientInfo \
(
    type       = enums.ClientType.IOS_MUSIC,
    name       = 'IOS_MUSIC',
    version    = '4.16.1',
    identifier = 'youtube-music-ios',
)

IosKids = models.ClientInfo \
(
    type    = enums.ClientType.IOS_KIDS,
    name    = 'IOS_KIDS',
    version = '5.42.2',
)

IosStudio = models.ClientInfo \
(
    type    = enums.ClientType.IOS_STUDIO,
    name    = 'IOS_CREATOR',
    version = '20.47.100',
)

Tv = models.ClientInfo \
(
    type       = enums.ClientType.TV,
    name       = 'TVHTML5',
    version    = '7.20210224.00.00',
    identifier = 'youtube-lr',
)
