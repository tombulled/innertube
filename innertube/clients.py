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

Web = models.ClientInfo \
(
    name       = 'WEB',
    version    = '2.20210223.09.00',
    identifier = 'youtube',
)

WebMusic = models.ClientInfo \
(
    name    = 'WEB_REMIX',
    version = '0.1',
)

WebKids = models.ClientInfo \
(
    name       = 'WEB_KIDS',
    version    = '2.1.3',
    identifier = 'youtube-pegasus-web',
)

WebStudio = models.ClientInfo \
(
    name    = 'WEB_CREATOR',
    version = '1.20210223.01.00',
)

Android = models.ClientInfo \
(
    name    = 'ANDROID',
    version = '16.07.34',
)

AndroidMusic = models.ClientInfo \
(
    name       = 'ANDROID_MUSIC',
    version    = '4.16.51',
    identifier = 'youtube-music-android',
)

AndroidKids = models.ClientInfo \
(
    name    = 'ANDROID_KIDS',
    version = '6.02.3',
)

AndroidStudio = models.ClientInfo \
(
    name    = 'ANDROID_CREATOR',
    version = '21.06.103',
)

Ios = models.ClientInfo \
(
    name    = 'IOS',
    version = '16.05.7',
)

IosMusic = models.ClientInfo \
(
    name       = 'IOS_MUSIC',
    version    = '4.16.1',
    identifier = 'youtube-music-ios',
)

IosKids = models.ClientInfo \
(
    name    = 'IOS_KIDS',
    version = '5.42.2',
)

IosStudio = models.ClientInfo \
(
    name    = 'IOS_CREATOR',
    version = '20.47.100',
)

Tv = models.ClientInfo \
(
    name       = 'TVHTML5',
    version    = '7.20210224.00.00',
    identifier = 'youtube-lr',
)
